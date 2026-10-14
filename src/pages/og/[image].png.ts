import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { BLOG_CARD_TITLE, socialImagePath } from '../../utils/social-image';
import { renderSocialImage } from '../../utils/render-social-image.mjs';

export const prerender = true;

export async function getStaticPaths() {
  const posts = await getCollection('writing', ({ data }) => !data.draft);
  const cards = [
    { title: BLOG_CARD_TITLE, article: false },
    ...posts.map(post => ({ title: post.data.title, article: true })),
  ];
  return Array.from(new Map(cards.map(card => [socialImagePath(card.title, card.article), card])).entries())
    .map(([path, props]) => ({ params: { image: path.split('/').pop()!.replace(/\.png$/, '') }, props }));
}

export const GET: APIRoute = async ({ props }) => {
  const image = await renderSocialImage(props.title, props.article);
  return new Response(new Uint8Array(image), { headers: { 'Content-Type': 'image/png' } });
};
