---
title: What I still own when AI writes the code
date: 2026-10-21
description: My thinking on coding with AI has moved on. The questions about judgment, ownership and doing the work well are still here.
category: Programming
tags: [ai, coding, craft, product]
draft: true
---

In January last year, I wrote about [turning off autocomplete](/writing/2025-01-03-thoughts-on-coding-with-ai/) and getting some of my rhythm back. AI was producing code, but the cleanup and the feeling that I hadn't quite made the thing myself were bothering me. I liked using it for refactoring. Giving it more of the work came with questions I wasn't ready to brush aside.

Well, quite a bit has changed since then!

Working on Hydra, I'm now using AI across implementation, reviews, product decisions. The conversation has moved well beyond finishing a line in my editor. I can ask for a feature to be investigated, have the tradeoffs explained, and work through an implementation without personally typing every part of it. That is a pretty big departure from where I was when I wrote that post.

I don't think my earlier discomfort was misplaced though. Looking back, the part that bothered me was how easy it had become to accept something without understanding it well enough. Being able to produce more of it hasn't made that question go away.

### Something still has to be decided

Recently, whilst planning staff access for Hydra's merchant app, I wanted the work broken down into small features that I could check individually. There were plenty of things we could have included. Team management, more permissions, different experiences for different people. Each addition sounded reasonable on its own, which is usually how these things get you.

We settled on two roles for the initial scope, admin and staff, and kept team management out of the mobile app. I also wanted to be deliberate about which models tackled which pieces, because spending more tokens isn't automatically getting more useful work done.

Those decisions happen before most of the code. Someone has to decide what the first version should allow, what can wait, and what would make the whole thing unnecessarily complicated. AI can help reason through that, but I still need a position on what we're trying to accomplish.

If I can't explain why a feature belongs, having it implemented quickly doesn't help me much.

### Small enough to check

One thing I'm becoming more particular about is the size of the work I hand over. A large request can come back with a large answer, lots of changed files, and a reassuring explanation of why it all fits together. There is then a fairly substantial job waiting for me: making sense of it.

I would rather check a sign-in flow, understand what a staff member can see, and then move on to what they can do. If something is wrong, the conversation is still about a small enough piece that we can deal with it properly. It also gives me a chance to change my mind before that decision has spread everywhere.

This feels familiar. Years ago, I wrote about [what I learnt from pairing](/writing/2017-08-06-further-takeways-from-pairing/), including doing less and asking questions until the reasoning made sense. I find myself coming back to those habits. The tool has changed quite dramatically; the usefulness of asking why has held up well.

### The feeling of ownership

I used to associate a lot of ownership with the process of writing the code. You struggle with something, figure it out, and the result feels like yours because you remember what it took to get there. There is satisfaction in that which I still value.

With AI involved, I'm having to be more precise about what I want to remain responsible for. Understanding the problem. Knowing what we've agreed to build. Looking at the result carefully enough to spot where it misses the point. Being able to explain a decision without just forwarding the answer I was given.

That last one is quite revealing, I think. If someone asks why the app behaves a certain way, how comfortable am I answering?

I still want to understand the software I'm putting into the world. I'm happy to have much more help creating it than I was before. Both of those things can be true, and working out the balance is probably going to keep me occupied for a while.

For now, I'm trying to keep the work small enough that I can stay curious about it. There is a lot of value in being able to stop and say, hang on, why are we doing that?
