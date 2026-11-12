#!/usr/bin/env python3
"""Create reviewable Buttondown drafts from the feed deployed by this workflow."""
import argparse
import hashlib
import html
import json
import os
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

API = 'https://api.buttondown.com/v1'
SITE = 'https://chikomukwenha.co'
ROOT = Path(__file__).resolve().parent.parent
PUBLICATION_TIMEZONE = ZoneInfo('Africa/Johannesburg')


def article_url(value):
    parsed = urlsplit(value)
    if (parsed.scheme != 'https' or parsed.netloc != 'chikomukwenha.co'
            or not re.fullmatch(r'/writing/[a-z0-9-]+/?', parsed.path)):
        raise ValueError('Expected a published article URL on chikomukwenha.co')
    return SITE + parsed.path.rstrip('/') + '/'


def read_feed(xml, now=None):
    now = now or datetime.now(timezone.utc)
    posts = {}
    for item in ET.fromstring(xml).findall('./channel/item'):
        url = article_url(item.findtext('link') or '')
        title = (item.findtext('title') or '').strip()
        date = parsedate_to_datetime(item.findtext('pubDate') or '')
        if not title or date.tzinfo is None:
            raise ValueError('Feed item needs a title and timezone-aware publication date')
        # Astro encodes date-only frontmatter at UTC midnight. Publication is
        # based on Chiko's local calendar day, including the first two hours.
        if date.astimezone(PUBLICATION_TIMEZONE).date() <= now.astimezone(PUBLICATION_TIMEZONE).date():
            posts[url] = {'url': url, 'title': title,
                          'description': item.findtext('description') or ''}
    return list(posts.values())


class Buttondown:
    def __init__(self, token):
        if not token:
            raise ValueError('Add the BUTTONDOWN_API_KEY Actions secret before running')
        self.token = token

    def request(self, method, path, payload=None, key=None):
        # The client deliberately exposes only read and draft-create operations.
        if method not in ('GET', 'POST') or (method == 'POST' and (
                path != '/emails' or payload.get('status') != 'draft'
                or 'publish_date' in payload)):
            raise ValueError('Only reads and unscheduled draft creation are allowed')
        headers = {'Authorization': f'Token {self.token}', 'Content-Type': 'application/json'}
        if key:
            headers['X-Idempotency-Key'] = key
        request = Request(API + path, method=method, headers=headers,
                          data=json.dumps(payload).encode() if payload is not None else None)
        try:
            with urlopen(request, timeout=30) as response:
                return json.load(response)
        except HTTPError as error:
            # Never dump headers, keys, response bodies or subscriber data in CI logs.
            raise RuntimeError(f'Buttondown API returned HTTP {error.code}; check key permissions and API requests') from None
        except (URLError, TimeoutError):
            raise RuntimeError('Buttondown API connection failed; rerun the workflow safely') from None

    def emails(self):
        emails, page = [], 1
        while True:
            data = self.request('GET', f'/emails?page={page}')
            batch = data['results']
            emails.extend(batch)
            if len(emails) >= data['count']:
                return emails
            if not batch:
                raise RuntimeError('Buttondown pagination ended before all emails were checked')
            page += 1

    def create(self, payload):
        key = 'blog-draft-' + hashlib.sha256(payload['canonical_url'].encode()).hexdigest()
        created = self.request('POST', '/emails', payload, key)
        confirmed = self.request('GET', '/emails/' + created['id'])
        if confirmed.get('status') != 'draft':
            raise RuntimeError('Buttondown did not confirm draft status; inspect the email before continuing')
        return confirmed


def existing_email(post, emails):
    for email in emails:
        canonical = email.get('canonical_url') or ''
        if canonical:
            try:
                if article_url(canonical) == post['url']:
                    return email
            except ValueError:
                pass
        # Also recognise the announcement already written by hand in Buttondown.
        body = html.unescape(email.get('body') or '')
        if re.search(re.escape(post['url'].rstrip('/')) + r'/?(?=[\s\"\'<>\)\]?]|$)', body):
            return email
    return None


def draft_payload(post, directory):
    slug = urlsplit(post['url']).path.strip('/').split('/')[-1]
    custom = directory / f'{slug}.md'
    body = custom.read_text().strip() if custom.exists() else (
        f"Hello!\n\nI've written a new post: {post['title']}.\n\n"
        f"{post['description']}\n\n[Read the post]({post['url']})\n\nChiko")
    if body.startswith('---'):
        raise ValueError('Newsletter copy should contain only the email body, without frontmatter')
    if post['url'] not in body:
        body += f"\n\n[Read the post]({post['url']})"
    return {'subject': post['title'], 'body': body, 'status': 'draft',
            'canonical_url': post['url']}


def sync(posts, baseline, directory, client=None, dry_run=False, only_url=None):
    baseline = {article_url(url) for url in baseline}
    candidates = [post for post in posts if (
        post['url'] == only_url if only_url else post['url'] not in baseline)]
    if only_url and not candidates:
        raise ValueError('Requested article is not in the published feed')
    if not candidates:
        return ['No new posts; no Buttondown drafts created.']
    # Validate every payload before any write, so malformed copy cannot partially run.
    payloads = [(post, draft_payload(post, directory)) for post in candidates]
    emails = client.emails() if client else []
    messages = []
    for post, payload in payloads:
        existing = existing_email(post, emails)
        if existing:
            messages.append(f"Already announced: {post['url']}")
        elif dry_run:
            messages.append(f"Would create draft: {post['url']}")
        else:
            created = client.create(payload)
            emails.append(created)
            messages.append('Draft ready for review: https://buttondown.com/emails/' + created['id'])
    return messages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--feed-file', default='dist/client/rss.xml')
    parser.add_argument('--dry-run', action='store_true', help='Never create or modify emails')
    parser.add_argument('--only-url', help='Check one published article, including a baseline article')
    args = parser.parse_args()
    posts = read_feed(Path(args.feed_file).read_bytes())
    baseline = json.loads((ROOT / 'newsletters/baseline.json').read_text())
    token = os.environ.get('BUTTONDOWN_API_KEY')
    # Live runs require credentials even when there are no new posts: validate setup.
    client = Buttondown(token) if token or not args.dry_run else None
    if client:
        # Check authentication/read permission even on the first run with no new posts.
        client.request('GET', '/emails?page=1')
    messages = sync(posts, baseline, ROOT / 'newsletters', client, args.dry_run,
                    article_url(args.only_url) if args.only_url else None)
    for message in messages:
        print(message)
    if summary := os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(summary, 'a') as output:
            output.write('## Buttondown drafts\n\n' + '\n'.join('- ' + m for m in messages) + '\n')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, RuntimeError, KeyError, OSError, ET.ParseError) as error:
        print(f'Newsletter draft sync failed: {error}', file=sys.stderr)
        sys.exit(1)
