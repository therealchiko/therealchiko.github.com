import { createHash } from 'node:crypto';

export const BLOG_CARD_TITLE = 'Making things well.';
export const CARD_VERSION = 'working-poster-v1';

export function socialImagePath(title = BLOG_CARD_TITLE, article = false) {
  const hash = createHash('sha256').update(`${CARD_VERSION}:${article}:${title}`).digest('hex').slice(0, 12);
  return `/og/${article ? 'article' : 'blog'}-${hash}.png`;
}
