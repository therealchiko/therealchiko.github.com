---
layout: post
title: "Getting rid of rdiff-backup's incremental backups"
tags: unix terminal automation
---
Recently I had to help with maintenance of a server that I didn't configure myself that had maxed out its storage (the horror!). Anyway, it took me some time to figure out it was using the handy and useful [rdiff-backup](http://rdiff-backup.nongnu.org/) package to create and store backups automatically. Rdiff-backup's mission is succinctly put as _an idea is to combine the best features of a mirror and an incremental backup_

As it turns out, rdiff-backup does come with a handy tool to configure it to delete backups that are x-days old e.g 4 weeks:

`rdiff-backup --remove-older-than 4W target-dir`

<!--more-->

Running that works like magic but I realized we could have an automated recipe to run a cron job right after each backup is saved. Let's proceed and do that:

touch /etc/cron.daily/remove_old.sh (don't forget to make it an executable)

```
#!/bin/bash
rdiff-backup --remove-older-than 4W target-dir
```

Now we configure our cronjob to run after the time when rdiff-backup has run its backup:

crontab -e
```
00 5 * * *  /etc/cron.daily/remove_old.sh
```

And that's it! We have a cron job that prunes our directory for space every day at 5am.

To test if your script runs, test cron jobs like so:

```
run-parts /etc/cron.daily
```


