---
title: "Uses, 2026: the software side"
date: 2026-10-28
description: An update to my Uses post, focused on Codex, Git, small features and the software workflow behind my current projects.
category: Programming
tags: [tools, workflow, ai, productivity]
draft: true
---

My [last Uses post](/writing/2021-11-21-uses/) was mostly about the things on and around my desk. Keyboards, monitors, a microphone I was very happy with, and enough equipment to make plugging everything into the laptop a project of its own.

This update is about the software side. Looking at the work I'm doing now, there's quite a bit to say about how I use the tools together, especially with AI involved. A list of app names would only tell part of that story.

### Codex and keeping context

I'm using Codex on Hydra and other software work, for implementation, investigation, reviews and talking through decisions. Sometimes the useful output is a change to the code. Sometimes it's finding the bit of the system that explains a confusing behaviour, or working out what a feature actually involves before agreeing to build it.

I want those conversations to stay close to the project. If we're discussing an existing flow, I want the answer grounded in what it does today. There is a lot of room to design a lovely solution to a slightly different problem when you skip that step!

I'm also paying more attention to the size of each request. For the merchant staff work, I asked for a plan broken into individual features that I could check as we went. That makes it easier to keep track of what has been decided and what is still open.

### Git, branches and worktrees

Git is still doing a lot of the quiet work. Branches and worktrees give separate changes somewhere to live whilst they're being worked on. With several project conversations going on, that separation matters. I need to know which version of the code we're discussing and where a particular change ended up.

One distinction that keeps coming up is whether something is changed locally, committed, pushed or actually deployed. Those are different stages, and "done" doesn't always tell me which one we're at. I find it helpful to ask directly, especially when I'm about to look for the result online.

### Choosing how much help a task needs

I've been thinking more about model choice and usage. There are tasks where I want deeper investigation, and others where the work is quite bounded once the decision has been made. I'd like the amount of attention spent to reflect that.

I'm still working out the balance. Using a smaller model for a straightforward piece sounds sensible, but any saving can disappear if the handoff is vague and we spend the next few conversations re-establishing the context. A clear task with a clear finish seems like a good place to start.

I also don't want to get so caught up in optimising usage that the work becomes unnecessarily complicated. The point is to finish a useful piece, understand it, and move on.

### Checking the thing itself

Tests and reviews are part of the process, and I still want to walk through the actual behaviour. Does the message say what the customer is trying to do? Can staff get to the right screen? Those questions bring the work back to the person using it.

I wrote years ago about [finishing well](/writing/2022-06-19-finishing/) making the next start easier. That feels relevant here too. Knowing what changed, what was checked and what is left gives me a much better place to pick up from than a long conversation ending in "all done."

So that's the current software edition. Quite a lot has changed since the desk tour, but I'm still interested in the same thing: putting together a working environment that helps me do the work properly, and figuring out which parts are making that harder than it needs to be.
