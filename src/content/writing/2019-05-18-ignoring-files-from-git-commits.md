---
layout: post
title: "Ignore changes to specific git files"
description: "git, code"
tags: [git, version-control, development-workflow, technical-tips]
categories: ["Programming"]
---

There are times when you are working on something that should not be committed even though it has changed. In this instance, it's not wise to add the changed files to `.gitignore`:

- maybe because the file(s) should always remain in the repo
- or suppose it's a config file with your private key for a service you are using locally, not everyone on the team even uses it.

Whatever the case, git has an easy way for this: `git update-index`! Here is how it works:

```bash
git update-index --assume-unchanged [path_to_file]
```

This simple rule will delist/hide all changes on that file in future commits. That means you are free to edit the file locally and the changes won't be staged nor pushed upstream! Listing the file again is straightforward:

```bash
git update-index --no-assume-unchanged [path_to_file]
```

Whilst the commands are handy, they do not come with an easy way to untrack an entire folder, which is not-great. However, this can be easily done by a bash command that can list all files you want to "untrack" locally and transverse that list, updating each file's entry in the git index.

Update-index is a command that does exactly what it describes, it tells git to update its index for the tracked file it is given. When we set that entry of the file in the index to `assume-unchanged` what that does is tell Git to simply ignore anything that happens to that file. This results in performance gains via unburdening Git from doing unnecessary indexing on files we no longer care about. However, keep in mind that should the file be changed upstream, when merging commits, Git will still ignore it locally so it does introduce an extra step to be aware of.

Lastly the commands are pretty long. An easy way I use to set them to something friendlier is by aliasing them in my `gitconfig` file as follows:

```bash
[alias]
assume-unchanged = update-index --assume-unchanged
assume-changed = update-index --no-assume-unchanged
```

After this change, you can easily call: `git assume-unchanged [file]`!

As always thank you for reading, if you have tips or advice or other ways you handle this, please fire away in the comments below.

<!--more-->
