#!/usr/bin/env python

# Jared Henry Oviatt

### missing bash builtins in searchs

sys.path.append("/usr/lib/howto");

import subprocess
import sys
import basics

def get_command(argv):

  search_terms = ['apropos', '-a'] # 0 term is command

  search_terms.extend(argv)
  
  return search_terms

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

  subprocess.call(SEARCH_COMMAND)

  return 0
  

if __name__ == '__main__':
  main(sys.argv[1:])

