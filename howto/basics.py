
#!/usr/bin/env python

# Jared Henry Oviatt

def switch(arg):

  if arg == "cd":
    return cd_cmd()
  if arg == "cp":
    return cp_cmd()
  if arg == "mv":
    return mv_cmd()
  if arg == "rm":
    return rm_cmd()
  if arg == "ls":
    return ls_cmd()
  if arg == "pwd":
    return pwd_cmd()
  if arg == "mkdir":
    return mkdir_cmd()
  else:
    return not_basic(arg)

  return

def basics(argv):
  # cd, cp, mv, rm, ls, pwd, mkdir

  if not argv:
    all_basics()

  for arg in argv:
    switch(arg)

  return 0
  
def all_basics():
  print "Some basic commands..."
  print ""
  cd_cmd()
  cp_cmd()
  mv_cmd()
  rm_cmd()
  ls_cmd()
  pwd_cmd()
  mkdir_cmd()
  return

def not_basic(cmd):
  print "Sorry, " + cmd +" isn't basic enough. Try 'howto'."
  return
    
def cd_cmd():
  print "'cd': change your current directory"
  print "- specify full or relative path"
  print "- 'cd' alone changes directory to home directory"
  print "- ex. -$ cd ~/Desktop/some_directory/"
  print ""
  return

def cp_cmd():
  print "'cp': copy file1 into file2"
  print "- specify file1 (source) and file2 (dest)"
  print "- ex. -$ cp original.py copy.py"
  print ""
  return

def mv_cmd():
  print "'mv': move file1 into file2 (or renames file1 as file2)"
  print "- specify file1 (source) and file2 (dest)"
  print "- ex. -$ mv original.py some_directory/moved_file.py"
  print ""
  return

def rm_cmd():
  print "'rm': remove a file or directory"
  print "- specify file or directory to remove"
  print "- use '-r' flag to remove a directory (recursively)"
  print "- use '-i' flag to require confirmation"
  print "- ex. -$ rm -r -i my_directory/"
  print ""
  return

def ls_cmd():
  print "'ls': list contents of a directory"
  print "- (optional) specify directory to list contents of"
  print "- use -l flag to list in long form"
  print "- use -a to include hidden files"
  print "- ex. -$ ls -a"
  print ""
  return

def mkdir_cmd():
  print "'mkdir': create directory"
  print "- specify new directory name"
  print "- ex. -$ mkdir my_new_directory"
  print ""
  return

def pwd_cmd():
  print "'pwd': print working directory"
  print "- ex. -$ pwd"
  print ""
  return

  return 0
