---
layout: post
title: How to theme Views output Drupal 6/7
categories: [drupal]
tags: [views, semantics]
---

I was recently asked by a friend how the output from Views can be themed easily. I'm going to show you an easy way for pure Drupal n00bs to control the look and feel of their website. This tutorial does not require much coding skill, just some CSS knowledge and the ability to use Views is enough.
<!--more-->

### Modules

[Views](http://www.drupal.org/project/views)

[Semantic Views](http://www.drupal.org/project/semanticviews)

Please download the above modules at their project pages. On a side note, get the recommended versions (usually these are ready for prime time on live sites.) For clarity's sake, I'm going to use a token **[yourwebsite]** as a substitute for your Drupal Website's URL.

1. After installing the modules go to the modules Admin page and enable them.

2. Visit the Views Admin page at [yourwebsite]**/admin/build/views**. Click **Add** and create a new view of **View Type: Node**. Click Next.

3. I hope you have some content on your website, if not you can use the [Devel](http://www.drupal.org/project/devel) module and auto generate some demo nodes.

4. Under fields in Views, Click Add to put some fields.

Choose the fields **Node: Body** and **Node: Title**. Don't bother with changing any other settings.

Rearrange the fields so that the Node Title is above the Node Body.

5. Now lets use Views Semantics for the styling. On the View's page go and click on **Style: Unformatted**, choose **Semantic Views** from the options that appear. Click **Update**.

6. From the settings that appear now, leave everything as is and Click Update again.

7. Now go and click **Row Style: Fields** link. Change the settings from Fields to **Semantic Views: Fields**. Click **Update** and you will be presented with options to define html tags and CSS class names on fields.

8. Click **Update** to save our style settings. Next go right ahead and Click **Save**. We are done with configuring a very simple View.

9. Next Up, lets style our View for a slick presentation. Copy the following code to your CSS files of your active theme.

```css
div.newbodyclass{

    background: none repeat scroll 0 0 #DDDDDD;
    
    margin: 12px;
    
    padding: 6px;

}

div.newnodetitle{
    
    border-bottom: 1px solid #BBBBBB;
    
    color: navy;
    
    font-weight: bold;
    
    padding-bottom: 4px;

}
```

10. Voila! We got our basic style for a View generated page now.

_I'd appreciate your feedback on this tutorial. This is part one of my tutorials on Views. To keep updated on new posts, follow me on Twitter [@therealchiko](http://www.twitter.com/therealchiko)_