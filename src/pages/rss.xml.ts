import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { getCollection } from 'astro:content';
import { sortPostsByDate, getPostDate } from '../utils/posts';
import { SITE_DESCRIPTION } from '../utils/site';

export async function GET(context: APIContext) {
  const posts = await getCollection('writing', ({ data }) => !data.draft);
  const sorted = sortPostsByDate(posts);

  return rss({
    title: 'Chiko Mukwenha',
    description: SITE_DESCRIPTION,
    site: context.site!,
    items: sorted.map((post) => ({
      title: post.data.title,
      pubDate: getPostDate(post),
      description: post.data.description || '',
      link: `/writing/${post.slug}/`,
    })),
  });
}
