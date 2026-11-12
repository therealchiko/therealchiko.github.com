# Newsletter drafts

After GitHub Pages deploys successfully from `main`, the deployment workflow
reads the exact RSS feed built for that release and creates Buttondown drafts.
It never publishes, schedules or sends an email. Review and send in Buttondown.
Buttondown's API supports draft creation on the Free plan:
https://docs.buttondown.com/drafting-emails-via-the-api

## One-time setup

Create a dedicated key at Buttondown → API → Keys. Set **Emails: Write**,
**Sending: None**, and every other permission to **None**. Add it to this
repository's Actions secrets as `BUTTONDOWN_API_KEY`. Never commit the key.
The workflow fails with a setup message if the secret is absent.

## Writing the announcement

Optionally add `newsletters/<post-slug>.md` alongside the blog post. This file
contains only the email body, with no frontmatter. Write the introduction in
your own voice and include the article's full URL. The script uses the article
title as the subject and adds a read link if the body doesn't already contain it.
Without a file, it creates a short editable draft from the title and description.
These files are not rendered as pages on the blog.

`baseline.json` records the 43 posts published before this automation was added,
including the Hydra article with its existing manual announcement. Leave this
list in place: those posts are skipped on normal deployments. Newly published
articles are considered automatically, regardless of when their source file was
created. Editing a published article does not replace a newsletter you've edited.
Future-dated feed entries are ignored until their publication date has passed
and the next deployment runs; there is no scheduled polling job.

## Verification and recovery

Run `python3 -m unittest discover -s scripts -p 'test_*.py'`.
After a site build, run `python3 scripts/buttondown_drafts.py --dry-run` to see
which articles are eligible without credentials or writes. With a key set in the
environment, dry runs also check for existing Buttondown emails.

The script recognises an existing email by its canonical article URL or an article
link in its body, including manual drafts and sent emails. It checks all API
pages, uses a stable `X-Idempotency-Key` per article when creating a draft, and
reads each new email back to verify draft status. Rerunning after an API failure
is safe; it does not overwrite existing email copy. Deleting a draft is not a
supported way to request a fresh announcement: restore/edit it in Buttondown.

For a manual check, run **Deploy to GitHub Pages** from the Actions tab. Set
`newsletter_dry_run` to true and optionally supply `newsletter_post_url` with a
published article URL. The URL option can also check a baseline article, and
still skips any matching email. Manual runs redeploy the blog before checking
drafts. Review the **Create Buttondown drafts** job summary for results and links.

If the draft job fails, the site deployment remains successful; fix the key or
content error and rerun the failed job. No send API endpoint is used, and the key
must have sending disabled as an independent safeguard.
