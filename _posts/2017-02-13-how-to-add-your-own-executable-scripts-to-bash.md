---
layout: post
title: "How to add your own executable scripts to bash"
tags: programming bash unix automation
---
I have been enjoying the book Effective Engineer by Edmond Lau. One of the great tricks of becoming more effective is to set workflows that make you do more, much faster. I have ended up setting a few scripts to automate a lot of bash commands such as ssh-ing, using git etcetera and in this short primer i'd love to show total newbies how to have your own executable scripts from any place on your system.

The first thing to note here is Mac OS has a few candidate files in your home folder that it indexes for commands to use in every bash window. On my system, I prefer to use ~/.bash_rc mainly because it is loaded up when a new instance of a terminal window is opened compared to ~/.bash_profile which is loaded up at login.
<!--more-->
Without further ado, let's create a small script that will shutdown the laptop when we type:

`c.restart`

### 1st Approach - using an alias
Easiest way to do this is to create an alias for the command you'd normally type in the terminal. Open up your ~/.bashrc and enter the following:

```bash
alias c.restart="sudo shutdown -r now"
```

Save the file and close. 
To have this command available in bash, in your terminal window enter:

```bash
source ~/.bashrc
```

You can test if it's working by typing **c.restart** after that you should be asked for password before your computer restarts. (Since this is just for demo purposes you can enter a wrong one three times if you don't want to restart).


### 2nd Approach - adding an executable script to your bin directory

What we are going to do here is add a private bin directory with all the scripts you'll later write. This is a good practice because it separates some important defaults from your own personal scripts you'd want to access easily.

First thing to do is to add the ~/bin directory to your PATH variable. Open up .bash_profile and add the following line:

```bash
export PATH="~/bin:$PATH"
```

Simply what we have done is added your own personal bin directory to the PATH variable which is used to look for scripts to execute when you submit a command to do something in your terminal.

Let's go ahead and create that directory:

```bash
mkdir ~/bin
```

Now any script we create in this folder will be easily accessible by name from the terminal. Let's go ahead and create our program, and call it just "c.restart":

```bash
#!/usr/bin/env bash

sudo shutdown -r now

```

After this, if you type: **c.restart** in your terminal it should ask for your password. If you enter it, your laptop should restart.

That's an easy way to add your own scripts that can automate a lot in your workflow and improve your efficiency. 

