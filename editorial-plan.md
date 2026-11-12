# Blog editorial plan

Focus future content on Hydra and software engineering. Do not write about Findable or finance-company operations, including anonymised payout stories. Preserve historical essays.

Publish new articles one week apart. Dates below are planned publication dates; drafts do not publish automatically.

| Planned date | Article | State |
| --- | --- | --- |
| 14 October 2026 | The work behind a simple customer experience | Included in the site build |
| 21 October 2026 | What I still own when AI writes the code | Draft |
| 28 October 2026 | Uses, 2026: the software side | Draft |
| 4 November 2026 | Finding Hydra's first customers | Draft |
| 11 November 2026 | Hydra's Railway outage and having a backup plan (working title) | Idea; needs incident details before drafting |

For the customer-acquisition draft, the confirmed starting points are door-to-door outreach, cold calling, arranging meetings with business owners, conversations with early users, and an offer to build the first client's website in return for three referral clients. As of 27 October, the offer has produced no clients; introductions and acceptance have not been confirmed. Update the outcome before publication if it changes. A specific early-user conversation would strengthen a later revision; obtain permission before identifying or quoting anyone.

For the outage follow-up, Chiko confirms builds continued during the Railway outage because the Pro plan was prioritised. The incident prompted thinking about redundancy, and Chiko wired a Slack app for notifications and health monitoring. Monitoring is implemented; redundant infrastructure has not been confirmed. Establish the incident date, any affected Hydra workflows, the signals the Slack app observes, and the fallback plan before writing a detailed incident account. Verify any provider-specific incident claims against Railway's incident report once the relevant outage is identified.

For each release, set the article's `draft` field to `false`, use the actual publication date if the plan changes, then build and deploy the site. Drafts are excluded from article routes, the homepage, the writing index, RSS and the generated sitemap.

When the AI follow-up is published, link to it from the January 2025 AI essay. When the software Uses article is published, add an update link to the 2021 Uses post. Keep those links out until their destinations are published.
