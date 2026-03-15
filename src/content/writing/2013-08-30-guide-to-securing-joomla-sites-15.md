---
layout: post
title: Guide to securing Joomla v1.5 sites
tags: [joomla, security, web-development, cms, best-practices]
categories: ["Programming"]
---

My Linux installation crashed this morning which got me thinking so much about doing regular backups and making sure everything is secure. It's been a weird week really, one of my mates got his website hacked too so I've had to think a lot on web security as well. I'm a Drupaler and he was running Joomla!, the CMS I dabbled in when I got started into web development. I hope to show you some of the cool things one can do to secure a Joomla! Site, with hacktivists on the prowl now more than ever (for better or worse) it helps to take measures against seeing the photo my friend woke up to find .
<!--more-->
**1.Use safe and secure extensions**

Joomla! Is open source with a large developer community. Whereas the positives of that far outweigh the negatives, it makes it a little vulnerable to poor written extensions that may otherwise be unsecure. To find if you are using safe and secure 3rd party extensions, check here:[http://docs.joomla.org/Vulnerable_Extensions_List](http://docs.joomla.org/Vulnerable_Extensions_List). It's a compiled list of vulnerable extensions. Bookmark it for future reference.

**2.Choose the best host**

It's useless to implement security features and host your website with a host which doesn't have proper security layers and offer easy access to hackers. It defeats all the work you might otherwise put in. A lot of hosts nowadays have well customized solutions for different CMSs, Joomla!, Drupal, etc. Ask around the Joomla! community for the best host in your location/country. Use this as refence:[http://resources.joomla.org/directory/support-services/hosting.html](http://resources.joomla.org/directory/support-services/hosting.html) Important: Make sure you ask if the server will have apache mod_php, fast-cgi, suphp or cgi.

**3.Quit Legacy mode**

To use the latest extensions in security, you need to install the latest extensions which take advantage of the most recent tricks and hacks. What happens when a developer codes is they create an extension compatible with the latest stable joomla release first. Full backwards compatibility is sometimes difficult to achieve because of the changes in the latest software iteration. Put simply, a latest software release fixes bugs and allows developers to do something they couldn't do with a previous version. Use native extensions.

**4. Folder permissions**

A lot of newbies have trouble knowing which permissions to have for different files and folders. It's even worse if you're moving between different Oss. Remember I said its important to know the hosting environment with regards to apache mod_php, fast-cgi, suphp or cgi? Well here's why:

a) mod_php

If the files have an owner other than nobody' or 'wwwrun' you need to make sure all change s are done only via ftp.

Use the following permissions:

DocumentRoot directory: 711 (e.g. public_html)  
Files: 644  
Directories: 755 (specify an owner for each of them)  
Cache and tmp directories: 777 (these directories will contain files owned by the web user - apache/nobody/wwwdata, etc)

b) If a Joomla! installation is hosted on apache with fast-cgi, suphp or cgi that runs as a different user, then you should set your permissions as follows:

DocumentRoot directory: 711 (e.g. public_html)  
PHP files: 600 (400 if you are truly paranoid)  
HTML and image files: 644 (444 if you are truly paranoid)  
Directories: 755 (711 if you are paranoid, but not for directories which need to be listed)  
Temp and cache directories: 700 (these are written as your user)

**6. Install [Jsecure](http://extensions.joomla.org/extensions/access-a-security/site-security/login-protection/12254)**

It's an extension tha hides the admin page. Just to give them a hard time if they want to try and use it to gain access :D

**13. Consider SEF URLs**

Search Engine Friendly (SEF) urls like article/blogpost instead of the default joomla urls make it harder for hackers to figure how the website is configured. They also help in making sure search engine crawlers to index your website easily. Find a good component to do this for you.

**14.Upgrade and back up regularly.**

Make sure you keep in touch with the latest instance of joomla. Do ugrades whenever there's a patch available. Backups should also be done often as well, you never when the site is take down by a hacktivist. Good web hosts do automated back ups but its always safe to have your own, relaunching the site will definitely take less time.

_Thanks for reading this article. Its part one of this series on Joomla! Security, follow me on Twitter @mukwenhac to keep updated on new content. I'd appreciate you leave a comment below._

Credits: The Joomla Wiki at: docs.joomla.org
