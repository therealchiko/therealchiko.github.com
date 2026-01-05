import type { CollectionEntry } from 'astro:content';

type Post = CollectionEntry<'writing'> | CollectionEntry<'building'>;

/**
 * Get the date from a post, falling back to extracting from slug/filename
 */
export function getPostDate(post: Post): Date {
  if (post.data.date) {
    return post.data.date;
  }

  // Extract date from slug (format: YYYY-MM-DD-title)
  const match = post.slug.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (match) {
    return new Date(`${match[1]}-${match[2]}-${match[3]}`);
  }

  // Fallback to current date
  return new Date();
}

/**
 * Sort posts by date (newest first)
 */
export function sortPostsByDate<T extends Post>(posts: T[]): T[] {
  return [...posts].sort((a, b) => getPostDate(b).getTime() - getPostDate(a).getTime());
}

/**
 * Get the category from a post (handles both category and categories fields)
 */
export function getPostCategory(post: CollectionEntry<'writing'>): string | undefined {
  if (post.data.category) {
    return post.data.category;
  }
  if (post.data.categories) {
    if (Array.isArray(post.data.categories)) {
      return post.data.categories[0];
    }
    return post.data.categories;
  }
  return undefined;
}
