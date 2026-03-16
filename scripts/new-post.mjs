#!/usr/bin/env node

/**
 * Creates a new blog post with frontmatter.
 *
 * Usage: npm run new-post "My Post Title"
 */

import { writeFileSync, existsSync } from 'fs';
import { join } from 'path';

const title = process.argv[2];

if (!title) {
  console.error('Usage: npm run new-post "My Post Title"');
  process.exit(1);
}

const slug = title
  .toLowerCase()
  .replace(/[^a-z0-9]+/g, '-')
  .replace(/^-|-$/g, '');

const today = new Date().toISOString().split('T')[0];
const filename = `${slug}.md`;
const filepath = join('src', 'content', 'writing', filename);

if (existsSync(filepath)) {
  console.error(`File already exists: ${filepath}`);
  process.exit(1);
}

const content = `---
title: "${title}"
date: ${today}
description: ""
draft: true
---

`;

writeFileSync(filepath, content);
console.log(`Created: ${filepath}`);
