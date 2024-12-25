---
layout: post
title: "Recent takeaways from pairing"
description: ""
tags: [pair-programming, vuejs, collaboration, learning-process, team-practices]
categories: ["Programming"]
---
A couple of weeks ago, my workmate paid a visit to Harare from his place in Cape Town for some pair programming, again (yay!). After having had a head start in coding a web app for a mobile application (built with Xamarin), the objective was to quickly knock it into shape and ship it out. I had chosen VueJS for the frontend (because it’s awesome), supported by an API in Laravel - to maintain consistency with the mobile app, we wanted everything to remain exactly the same. During the time of pairing, I learned even more lessons than the other times when I have paired with other programmers.
<!--more-->
Here are a few of my main takeaways:

### 1\. Do less

I was constantly reminded of how the best programmers have less to focus on. A change of context, is a huge price to pay. For example, on Jannie’s desktop, he uses it as an actual physical desktop, that means he one has ONE thing on there that he’d be working on! I thought that was genius as sometimes I struggle between juggling different projects. The simple fix here, is really, out of sight - out of mind. As simple as that!

As a result of this, I simplified my work environment by getting rid of Homestead in preference to Laravel Valet, and quickly hashed out a script that allows one to get and store whatever project you want to work on. You can grab it here: [bash script](https://gist.github.com/therealchiko/a7bdfeb961e18056e3d7986661d0a140)

### 2\. It’s all about maintenance

During the time, we got to discuss about tools and which ones make sense and the whys behind that. In Jannie’s mind, as far as I could read, it all boils down to maintenance and doing things easier. He was very clear that frameworks succeed not because of any sort of flashy-thing, but because they are solving current problems, better or in a much more easier way to manage. This little tidbit, helped give me context why we have so many competing frameworks and the pitfalls of just following any one thing because it’s deemed “hot”. One has to take the time to know why it’s hot, on a more practical, applicable way to your problems. Don’t code blindly, ask questions.

### 3\. There are no stupid questions

Being able to ask why x is x and not called y is just a good feeling! To get the most from pairing with someone who is better, I’d say ask away to get all the context and understanding you need. I think it really defeats the purpose of pairing if you still walk away from a session with questions in your head because you let your ego in the way.

### 4\. Good code is produced in cycles

This is sage advice but something we constantly overlook. Good code is not written the first time you write something. In our case, i discovered once the tests are green, that’s when real learning occurred when we started tweaking for performance, maintainability and documenting the reasons why we chose one method over the other.

There are more lessons to share, that are more technical than this one so keep an eye for my next few posts. Thanks for reading!
