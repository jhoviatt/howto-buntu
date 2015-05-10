#!/usr/bin/env python

# Jared Henry Oviatt

### missing bash builtins in searchs


import subprocess
import sys

sys.path.append("/usr/lib/howto");

import basics 

def get_command(argv):

  search_terms = ['apropos', '-a']

  search_terms.extend(argv)
  
  return search_terms

def check_results(argv):
  
  command = get_command(argv)

  results = subprocess.check_output(command)

  command = get_command(argv)

  if not results:
    y_or_n = raw_input("No results found: google it? (y/n) : ")
    if y_or_n.lower() == "y":
      ghow_command = ['ghow']
      ghow_command.extend(command[2:])
      subprocess.call(ghow_command)
      return
    elif y_or_n.lower() == "n":
      return
    else:
      print "Sorry, input not recognized: not 'Y/y' or 'N/n'"
      return

  print ""
  print "Didn't find what you were looking for? Try ghow instead."
  print ""

  return
  

def get_help():
  print "Type: 'howto basics' for basic commands"
  print "Type: 'howto' followed by search terms to search the man pages"
  return 0

def main(argv):

  if not argv:
    print "I need something to search for!"
    return 1
  if argv[0] == "basics":
    basics.basics(argv[1:])
    return 0
  elif len(argv) == 1:
    if argv[0] == "help":
      get_help()
      return 0
  
  SEARCH_COMMAND = get_command(argv) # gets command from args

  print ""
  subprocess.call(SEARCH_COMMAND)

  check_results(argv)

  return 0
  

if __name__ == '__main__':
  main(sys.argv[1:])

