# Writing Blog Posts

## Quick Start

Create a new markdown file in `src/content/writing/` with this naming format:

```
YYYY-MM-DD-your-post-slug.md
```

Example: `2025-01-05-launching-my-first-saas.md`

---

## Frontmatter

Every post needs frontmatter at the top:

```yaml
---
title: "Your Post Title"
description: "A brief summary for SEO and previews"
date: 2025-01-05
tags: ["startup", "building", "lessons"]
category: "Building"
draft: false
project: "contentboost"  # Optional: links post to a project
---
```

### Required Fields

| Field | Description |
|-------|-------------|
| `title` | The post title (shown on homepage and post page) |

### Optional Fields

| Field | Description | Default |
|-------|-------------|---------|
| `description` | SEO description and preview text | Empty |
| `date` | Publication date (YYYY-MM-DD) | Parsed from filename |
| `tags` | Array of tags for categorization | `[]` |
| `category` | Single category string | Empty |
| `draft` | Set `true` to hide from listings | `false` |
| `project` | Link to a project journey (see below) | Empty |

---

## Linking Posts to Projects

Posts can be automatically included in a project's journey timeline by adding the `project` field:

```yaml
---
title: "How I got my first customer"
project: "contentboost"
---
```

### Available Project IDs

| Project | ID | Page |
|---------|-----|------|
| contentboo.st | `contentboost` | `/building/contentboost` |
| usekeeptabs.com | `keeptabs` | `/building/keeptabs` |

When you add `project: "contentboost"` to a post:
1. It appears in **Recent Writing** on the homepage
2. It appears in the **contentboost journey timeline** at `/building/contentboost`
3. It's marked with a "post" type in the timeline

---

## Project Journey Updates

For non-blog updates (milestones, revenue events, etc.), edit `src/data/metrics.json`:

```json
{
  "projects": [
    {
      "id": "contentboost",
      "name": "contentboo.st",
      "journey": [
        {
          "date": "2025-01-05",
          "type": "milestone",
          "title": "Launched v2.0",
          "description": "Major redesign with new features"
        },
        {
          "date": "2025-01-10",
          "type": "revenue",
          "title": "Hit $1k MRR",
          "description": "First major revenue milestone!"
        }
      ]
    }
  ]
}
```

### Journey Entry Types

| Type | Use for |
|------|---------|
| `milestone` | Product launches, feature releases, pivots |
| `revenue` | Sales, MRR milestones, funding |
| `post` | Auto-added for linked blog posts |

---

## Where Posts Appear

| Location | What shows |
|----------|------------|
| `/writing` | All published posts (newest first) |
| Homepage "Recent Writing" | Latest 3 posts |
| `/building/[project]` | Posts with matching `project` field, merged with journey |

---

## Examples

### Regular blog post

```yaml
---
title: "Thoughts on coding with AI"
description: "When to use AI and when to code yourself"
tags: ["ai", "coding", "programming"]
category: "Programming"
---
```

### Project-linked post

```yaml
---
title: "Why I pivoted contentboost"
description: "The hard decision to change direction"
tags: ["startup", "pivot", "lessons"]
category: "Building"
project: "contentboost"
---
```

### Draft post (hidden)

```yaml
---
title: "Work in progress"
draft: true
---
```

---

## File Structure

```
src/
├── content/
│   └── writing/           # All blog posts go here
│       ├── 2025-01-05-my-post.md
│       └── ...
├── data/
│   └── metrics.json       # Project data and journey updates
└── pages/
    ├── writing/
    │   ├── index.astro    # /writing listing page
    │   └── [...slug].astro # Individual post pages
    └── building/
        ├── index.astro    # /building projects listing
        └── [projectId].astro # Individual project pages
```
