---
title: The work behind a simple customer experience
date: 2026-10-14
description: A little context on Hydra, and the decisions behind making customer retention straightforward for customers and merchants.
category: Product
tags: [hydra, product, entrepreneurship, simplicity]
draft: false
---

I've mentioned Hydra on this site without saying much about what I'm actually doing with it. Given how much of my attention it takes up, that's a bit of an omission!

[Hydra](https://usehydra.co.za) is focused on helping South African businesses bring customers back. The work includes rewards, joining through WhatsApp, and the merchant tools behind that experience. What interests me is how all these pieces fit into the ordinary running of a business. There can be quite a distance between having a feature and making it convenient enough for someone to use.

It's easy to describe a journey in a few words. A customer scans a code, joins a business, and can start participating in its rewards programme. As a description, that's fairly tidy. Building it means being much more specific about what happens at each step.

### Start with what the person is doing

One of the things we've been working through is the first WhatsApp message. A person is trying to join. The language needs to help them do that, without sending them into a conversation about a demo or something else they weren't asking for.

That might seem like a small copy change, but the first message is part of the product. If we introduce the wrong expectation there, the rest of the flow has to recover from it. I think developers can underestimate this because it doesn't look as substantial as adding a new screen or endpoint. Yet a few words can determine whether the next action is obvious.

Then there is the business the customer is joining. A phone number may interact with more than one business, so we have to be clear about which relationship we're talking about. From the customer's side, this should feel straightforward. Underneath it, we need to know exactly what happened.

This is the kind of detail I find myself paying attention to. QR codes, NFC and WhatsApp make for a useful way to demonstrate the journey, but the experience has to keep making sense after that first interaction too.

### Someone has to run it

The merchant side brings another set of questions. Who can look up a member? Who can record an action? What should staff see when they sign in, and what belongs with the owner?

Recently, we've been planning how to bring staff workflows into the Merchant app. The initial scope is deliberately small: two roles, admin and staff. Staff need the tools to work with members and record configured actions. We're leaving account management out of this first mobile scope, including the ability for admins to create or change staff accounts inside the app.

That's a plan we're working through, rather than a claim that all of it has shipped. I wanted it split into features I could check one at a time before moving on. There is enough to get right in the actual member workflow without also building a much broader permissions system.

Even something as ordinary as retrying after a timeout needs care when points are involved. The person may be pressing the button again because the app didn't give them a clear answer. We need to account for that possibility without awarding the same thing twice. These are the details that make an interface dependable once someone is using it for real work.

### Keeping the promise manageable

I enjoy the possibilities when building something new, which is probably why I have to be quite deliberate about scope. It's easy to see where the product could go. Every new option introduces more behaviour to explain, verify and maintain, and eventually someone has to use all this stuff whilst doing their job.

For Hydra, I'm trying to keep coming back to the actual interaction. Can a customer understand how to join? Can the person helping them find what they need? Is it clear what has happened and what happens next?

Those questions give me useful work to do even when the feature list looks complete. They also give a bit of context to what I mean when I say I'm building Hydra. A lot of it is this: looking closely at a fairly ordinary moment and trying to make it go well.
