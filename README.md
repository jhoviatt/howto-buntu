# howto-buntu

*Okay, yes. I know there are other Linux distros.*


___________________________________________________________________


This project was inspired by [this post](http://www.reddit.com/r/Lightbulb/comments/336hkl/google_terminal_for_linux_for_newbies_that_dont/) on reddit asking for a Google terminal for Linux.
However: if you're going to be *googling* about how to use the terminal, why not use the *terminal* to the learn the terminal!

Linux has `man-pages` built into the system, containing way too much information on how to use the terminal and what commands are possible. Like some lost, ancient library the `man-pages` stand in the depths of the system, begging to be parsed and read. 

There are even existing tools that can be used to search the man pages, such as the `man -k` command. Though something like this can be overwhelming to a beginner, as a search for 'change directory' returns some 200 potential results in a wall of text.

There are other tools that some have built (such as [this neat site](http://explainshell.com/)), allowing you tolearn about commands through their man descriptions, though this isn't exactly useful for a beginner who doesn't know that `cd` even *is* a command.

#### How about something in between?

Ideally, this project would bring a user friendly `howto` search tool to the command line, returning a pleasant set of 2 to 10 search results, and offering a google search if less are found. In addition, it would add a  `ghow` direct google search capability from the command line returning the top few hits with links and summaries.

-----------------------------------------------------------

### Installation Instructions

###### Git Clone to your computer.
1. Alternatively, click on **Download ZIP** on the right hand side of the page.
2. Next, you need to navigate into the directory where the clone is located.

###### Run the install commands
1. Run the command `sudo ./package.sh` to generate the install (.deb) package.
2. Run the command `sudo dpkg -i /dist/howto-buntu-X.X.X.deb` The 'X's here are the version number. Look at the file if you're not sure. Current version is 0.0.1 .
3. Lastly, run the command `sudo apt-get install -f` to install howto-buntu on your computer!

Or, if you're still confused see the [Complete Beginners Guide to Installing..](https://github.com/underscorejho/howto-buntu/wiki/Beginners%27-guide-to-installing-howto-buntu).

###### Now you can...
* Google away using the command `ghow` followed by search terms! (ex. `-$ ghow change directory`)
* Search the man pages with `howto` folled by search terms, or learn some basics with `howto basics`!

