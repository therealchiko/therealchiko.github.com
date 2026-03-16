import { defineCollection, z } from 'astro:content';

// Helper to handle tags as string or array
const tagsSchema = z.union([z.string(), z.array(z.string())]).optional().transform(val => {
  if (!val) return [];
  if (Array.isArray(val)) return val;
  return [val];
});

const writing = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.coerce.date().optional(),
    category: z.string().optional(),
    categories: z.union([z.string(), z.array(z.string())]).optional(),
    tags: tagsSchema,
    description: z.string().optional(),
    draft: z.boolean().optional().default(false),
    project: z.string().optional(), // Link post to a project (e.g., "contentboost", "keeptabs")
  }),
});

export const collections = { writing };
