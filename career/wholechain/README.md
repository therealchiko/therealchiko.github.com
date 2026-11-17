# Wholechain CV draft

The editable source is `cv.md`. The rendered application draft is
`../../output/pdf/Chiko_Mukwenha_CV_Wholechain.pdf`. These files are outside the
blog's `src/content` and `public` directories and are not included in site pages.

## Rebuild

Requires ReportLab. Newsreader and Manrope font files are bundled in `fonts/`
with their SIL Open Font Licenses; no system fonts or network access are needed
to render:

```sh
python3 career/wholechain/render_cv.py
```

## Presentation

Newsreader provides the name; Manrope provides semibold employer headings,
regular job titles, body text, metadata, and section labels. Static TrueType files were obtained through
Google Fonts, using regular and semibold weights, and are embedded in the PDF.
Sources: [Newsreader](https://fonts.google.com/specimen/Newsreader) and
[Manrope](https://fonts.google.com/specimen/Manrope). The layout uses white space,
slate text, fine grey rules, a separate date column, and compact earlier roles.
Primary experience stays on page one; technical expertise starts page two.
A zero-padding document frame aligns section labels, profile text, rules, and
the date column to the same 48-point margin; role text uses a shared inset.

## Editorial decisions

Lead with React, TypeScript, product delivery, and accessibility. Keep the
current Hydra role, Customer.io migration, and ContentBoost's Next.js/Polaris
work on page one. Restore JaSure's session-recording-informed UI overhaul,
KeepTabs' MVP scoping, and Langham's prototype feedback from the older CV.
Retain verified scope figures from the 2026 CV but omit the older percentage
claims. Retain the newer CV's Customer.io title; no title change was supplied.

## Evidence and public research

Reviewed on 17 November 2026:

- Original CV: `/Users/chiko/Downloads/Chiko_Mukwenha_CV_2026.pdf`.
- Older CV: `/Users/chiko/Downloads/Chiko_Mukwenha_CV_v4.pdf`.
- Chiko confirms a substantial personal contribution to Customer.io's large
  Ember-to-React migration and attention to WCAG in frontend work.
- [Wholechain's role](https://wholechain.com/careers/senior-frontend-react-engineer)
  prioritises React/TypeScript, product/design collaboration, reusable components,
  accessibility, testing, APIs, and production ownership.
- [Customer.io's own Product/AI posting](https://job-boards.greenhouse.io/customerio/jobs/7776591)
  names React, TypeScript, Go, and Ember, with frontend polish, product judgment,
  and end-to-end ownership. This is current company context, not proof of Chiko's
  individual responsibilities or the tools used during 2021-2024.
- [Pluma's technical overview](https://pluma.customer.io/overview/about)
  describes React and Ember APIs, shared TypeScript types, Storybook,
  designer/engineer review, and accessibility following WCAG 2.2. These current
  practices do not establish that Chiko used or built Pluma or worked to
  WCAG 2.2 during his tenure. Neither claim is included in the CV. Storybook
  experience is independently confirmed by Chiko.

The public material supports the React/Ember and accessibility context. It does
not independently establish the migration's timeline, completion, or Chiko's
individual contribution. Those details come from Chiko.

## Follow-up details confirmed by Chiko

Chiko confirms Platforms team membership, integration work, customisations to
the React-Ember bridge, building and maintaining the design library, Jest,
Storybook, atomic CSS, bento grid layouts, and substantial performance work.
He used FullStory and Mixpanel to inform decisions. Subsequent clarification
confirms JaSure used React Native and Hydra uses React through Next.js. Accessible forms and
keyboard navigation were priorities. Hydra started in 2026. The restored
JaSure and Langham UX work is accurate without the older percentage claims.

The CV selects the most relevant details; it does not claim ownership of the
entire migration, name the component library Pluma, specify a state-management
library, claim a measured speed improvement, or claim WCAG conformance.
Exact migration dates and accessibility verification tools remain unspecified;
they are not needed for the current supported wording. No start month for
Hydra is assumed. Retain "Software Engineer - Promoted to L3" from the 2026 CV.

## Verification

Rendered to two A4 pages; both pages inspected visually. Text extraction checked
for readable order and complete content. Contact fields are PDF hyperlinks.
Original PDFs were not modified.
