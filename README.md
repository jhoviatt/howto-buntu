# howto-buntu

*Okay, yes. I know there are other Linux distros.*


___________________________________________________________________


This project was inspired by [this post](http://www.reddit.com/r/Lightbulb/comments/336hkl/google_terminal_for_linux_for_newbies_that_dont/) on reddit asking for a Google terminal for Linux.
However: if you're going to be *googling* about how to use the terminal, why not use the *terminal* to the learn the terminal!

Linux has `man-pages` built into the system, containing way too much information on how to use the terminal and what commands are possible. Like some lost, ancient library the `man-pages` stand in the depths of the system, begging to be parsed and read. 

There are even existing tools that can be used to search the man pages, such as the `man -k` command. Though something like this can be overwhelming to a beginner, as a search for 'change directory' returns some 200 potential results in a wall of text.

There are other tools that some have built (such as [this neat site](http://explainshell.com/)), allowing you tolearn about commands through their man descriptions, though this isn't exactly useful for a beginner who doesn't know that `cd` even *is* a command.

#### How about something in between?

Ideally, this project would bring a user friendly `howto` search tool to the command line, returning a pleasant set of 2 to 10 search results, and offering a google search if less are found. In addition, it would add a `googlehowto` (with alias `ghow`) direct google search capability from the command line returning the top few hits with links and summaries.

-----------------------------------------------------------

###`googlehowto` Install instructions

1. `git clone` to a local directory of your choice (or fork it, then clone)
2. make sure you have Beautiful Soup installed
3. add the following to your ~/.bashrc:
    alias googlehowto='python $HOME/bin/ghow.py'
    alias ghow='googlehowto'
4. run `./ghow_install.sh` - use the command `chmod u+x ghow_install.sh` if you do not have execute privelages already
5. google away using the command `ghow` or `googlehowto` followed by search terms! (ex. `-$ ghow change directory`)


###`howto` Install instructions

1. `git clone` to a local directory of your choice (or fork it, then clone)
2. make sure you have Beautiful Soup installed
3. add the following to your ~/.bashrc:
    alias howto='python $HOME/bin/howto.py'
4. run `./howto_install.sh` - use the command `chmod u+x howto_install.sh` if you do not have execute privelages already
5. search the man pages with `howto` folled by search terms, or learn some basics with `howto basics`!
