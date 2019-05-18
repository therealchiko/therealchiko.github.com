---
layout: post
title: "Ignore changes to specific git files"
description: "git, code"
tags: []
---

There are times when you are working on something that should not be committed even though it has changed. In this instance, it's often not wise to add the changed files to the `.gitignore`, maybe because the file(s) should always remain in the repo or let's say suppose it's a config file with your own private key for an additional service you are using locally, not everyone on the team even uses it. Whatever the case, git has an easy way for this: `git update-index`! Here is how it works:

```bash
git update-index --assume-unchanged [path_to_file]
```

This simple rule will delist/hide all changed files from future commits. That means you are free to edit them locally and the changes won't be staged nor pushed upstream! Listing the file(s) is just as straightforward and is enabled by:

```bash
git update-index --no-assume-unchanged [path_to_file]
```

Whilst this command is handy, it does not come with an easy way to untrack an entire folder, which is kind of not-great. However, this can be easily done by a bash command that can list and transverse through the file list, updating each file's entry in the git index. (Challenge: give yourself a shot and see if you can create this type of command. I'm happy to share my solution to those that attempt and leave a comment, or ping me anyhow! )

Update-index is a command that does exactly what it describes, it tells git to update its index for tracked files. When we set it to `assume-unchanged` what that does is set a property in the index, for the file to not be checked for any changes. This of course means there are performance gains to this approach with unburdening git from doing unnecessary indexing. However, keep in mind that should the file be changed upstream, when merging commits git will still ignore it locally so it does introduce an extra step to be aware of.

Lastly the commands are pretty long. Easy way I use is to set them to something friendlier by aliasing them in my `gitconfig` file as follows:

```bash
[alias]
assume-unchanged = update-index --assume-unchanged
assume-changed = update-index --no-assume-unchanged
```

After this change, you can easily call: `git assume-unchanged [file]`!

As always thanks for reading, if you have tips or advice or specific other ways you handle this please fire away in the comments below!

<!--more-->
