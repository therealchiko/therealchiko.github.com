---
title: Removing all-day label from Drupal calendar module
tags: drupal coding php
layout: post
---

If you're new to Drupal, let me tell you something, the [Date](http://drupal.org/project/date) module is a must-install! It comes with some awesome functionality and a date API that enables you to add date fields to different content types, even entities in Drupal 7! 
<!--more-->
Installing and configuring is a breeze, just like any other Drupal module. However, there's a minor "bug" I discovered that really irked me enough to warrant an hour long search on how to fix it. The date module allows you to specify the date of when an "event" is going to occur. When entering the date however, by default it expects you to provide the dates and times as well. Leaving the time field blank will result in the field label including the text "All Day". Depending on your needs, you might find this inconvenient. So how is it fixed? Well, the fix is actually simple: Copy the following code to your template.php in your active theme folder:


```php
<?php
function YOUR-THEME-NAME_preprocess_date_all_day_label()
 { 
    return ""; 
 }
```
This will ensure the "All day" label goes away! More on how this is accomplished in the next blog post on Drupal 7's Preprocess Functions!
