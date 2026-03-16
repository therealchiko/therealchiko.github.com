import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { getCollection } from 'astro:content';
import { sortPostsByDate, getPostDate } from '../utils/posts';

export async function GET(context: APIContext) {
  const posts = await getCollection('writing', ({ data }) => !data.draft);
  const sorted = sortPostsByDate(posts);

  return rss({
    title: 'Chiko Mukwenha',
    description: "Writing about making things well in a world that's moving fast.",
    site: context.site!,
    items: sorted.map((post) => ({
      title: post.data.title,
      pubDate: getPostDate(post),
      description: post.data.description || '',
      link: `/writing/${post.slug}/`,
    })),
  });
}
