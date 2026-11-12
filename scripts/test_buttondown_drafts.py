from datetime import datetime, timezone
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from buttondown_drafts import Buttondown, draft_payload, existing_email, read_feed, sync

URL = 'https://chikomukwenha.co/writing/new-essay/'
POST = {'url': URL, 'title': 'New essay', 'description': 'A personal introduction.'}


class FakeClient:
    def __init__(self, emails=()):
        self.saved = list(emails)
        self.writes = []

    def emails(self):
        return list(self.saved)

    def create(self, payload):
        self.writes.append(payload)
        result = dict(payload, id='em_test')
        self.saved.append(result)
        return result


class DraftTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def test_baseline_does_not_create_backlog(self):
        client = FakeClient()
        sync([POST], [URL], self.directory, client)
        self.assertEqual(client.writes, [])

    def test_new_post_creates_only_an_unscheduled_draft_and_repeat_skips_it(self):
        client = FakeClient()
        sync([POST], [], self.directory, client)
        sync([POST], [], self.directory, client)
        self.assertEqual(len(client.writes), 1)
        self.assertEqual(client.writes[0]['status'], 'draft')
        self.assertNotIn('publish_date', client.writes[0])
        self.assertEqual(client.writes[0]['canonical_url'], URL)

    def test_manual_draft_with_html_link_is_recognised(self):
        client = FakeClient([{'id': 'manual', 'body': f'<a href="{URL}?utm_source=email">Read</a>'}])
        sync([POST], [], self.directory, client)
        self.assertEqual(client.writes, [])
        self.assertIsNone(existing_email(POST, [{'body': URL.rstrip('/') + '-other/'}]))

    def test_custom_copy_is_preserved_and_missing_link_is_added(self):
        (self.directory / 'new-essay.md').write_text('Hello!\n\nMy own words.\n\nChiko')
        payload = draft_payload(POST, self.directory)
        self.assertIn('My own words.', payload['body'])
        self.assertIn(URL, payload['body'])

    def test_dry_run_never_writes_and_only_url_can_check_a_baseline_post(self):
        client = FakeClient()
        result = sync([POST], [URL], self.directory, client, dry_run=True, only_url=URL)
        self.assertIn('Would create draft', result[0])
        self.assertEqual(client.writes, [])

    def test_invalid_copy_aborts_before_any_writes(self):
        second = dict(POST, url=URL.replace('new-essay', 'another'))
        (self.directory / 'another.md').write_text('---\ntitle: unwanted frontmatter\n---')
        client = FakeClient()
        with self.assertRaises(ValueError):
            sync([POST, second], [], self.directory, client)
        self.assertEqual(client.writes, [])

    def test_feed_excludes_future_posts_and_rejects_foreign_links(self):
        xml = f'<rss><channel><item><title>New &amp; useful</title><link>{URL}</link><pubDate>Fri, 13 Nov 2099 00:00:00 GMT</pubDate></item></channel></rss>'
        self.assertEqual(read_feed(xml), [])
        with self.assertRaises(ValueError):
            read_feed(xml.replace('chikomukwenha.co', 'example.com'))

    def test_publication_day_uses_johannesburg_even_before_utc_midnight(self):
        xml = f'<rss><channel><item><title>New</title><link>{URL}</link><pubDate>Fri, 13 Nov 2026 00:00:00 GMT</pubDate></item></channel></rss>'
        now = datetime(2026, 11, 12, 23, 0, tzinfo=timezone.utc)
        self.assertEqual(len(read_feed(xml, now)), 1)

    def test_client_refuses_missing_key_and_send_or_schedule_requests(self):
        with self.assertRaises(ValueError):
            Buttondown('')
        client = Buttondown('test-key')
        for path, payload in [('/emails', {'status': 'sent'}),
                              ('/emails/test/send-draft', {'status': 'draft'}),
                              ('/emails', {'status': 'draft', 'publish_date': '2099-01-01'})]:
            with self.assertRaises(ValueError):
                client.request('POST', path, payload)

    def test_pagination_checks_all_emails(self):
        client = Buttondown('test-key')
        with patch.object(client, 'request', side_effect=[
                {'results': [{'id': 'one'}], 'count': 2},
                {'results': [{'id': 'two'}], 'count': 2}]) as request:
            self.assertEqual(len(client.emails()), 2)
            self.assertEqual(request.call_args_list[1].args[1], '/emails?page=2')

    def test_create_uses_stable_idempotency_key_and_verifies_draft(self):
        client = Buttondown('test-key')
        payload = draft_payload(POST, self.directory)
        with patch.object(client, 'request', side_effect=[{'id': 'em_one'}, {'id': 'em_one', 'status': 'draft'}]) as request:
            client.create(payload)
            self.assertTrue(request.call_args_list[0].args[3].startswith('blog-draft-'))
            self.assertEqual(request.call_args_list[1].args, ('GET', '/emails/em_one'))
        with patch.object(client, 'request', side_effect=[{'id': 'em_one'}, {'status': 'sent'}]):
            with self.assertRaises(RuntimeError):
                client.create(payload)

    def test_api_errors_do_not_expose_response_or_key(self):
        client = Buttondown('private-token')
        with patch('buttondown_drafts.urlopen', side_effect=HTTPError('url', 403, 'private-token', {}, None)):
            with self.assertRaises(RuntimeError) as error:
                client.request('GET', '/emails')
        self.assertNotIn('private-token', str(error.exception))


if __name__ == '__main__':
    unittest.main()
