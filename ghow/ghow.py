
#!/usr/bin/env python

# Jared Henry Oviatt

import requests
from bs4 import BeautifulSoup

import sys


def get_url(argv):

  search_terms = []
  search_url = "https://www.google.com/search?q="

  # put args (words) in a list
  for each_arg in argv:
    search_terms.append(str(each_arg))
  
  # make a url out of list
  for each_item in search_terms:
    search_url += each_item
    search_url += "+"
  search_url = search_url[:-1] # remove trailing '+'
  print "search url: " + search_url
  
  return search_url

def print_results(soup): 
  
  # a result is in a <li> item with class="g"
  # in a <li>, need to print...
  ## <div class="rc">
  ### <h3 class="r">
  #### <a>                         # result title
  ### <div class="s">
  #### <div>
  ##### <div class="f kv _SWb">    # result link
  ##### <span class="st">          # result description

  #print soup.prettify() # raw soup

  print ""
  print "===================================================================="

  RESULT_TITLE=soup.find_all(class_="r")
  for TITLE in RESULT_TITLE:
    print TITLE.a.get_text()
    RESULT_LINK=TITLE.a['href']
    print str(RESULT_LINK)[7:]

  RESULT_DESC=soup.find_all(class_="st")
  for DESC in RESULT_DESC:
    print DESC.get_text()

  print "===================================================================="
  print ""
  
  return

def get_results(url):
  
  page = requests.get(url).content

  soup = BeautifulSoup(page)
  
  results = soup.find_all(class_="g", limit=5)
  
  for result in results:
    print_results(result)

  return soup


def main(argv):

  if not argv:
    print "I need something to search for!"
    return 1
  
  SEARCH_URL = get_url(argv) # gets url from args

  get_results(SEARCH_URL)

  return 0
  

if __name__ == '__main__':
  main(sys.argv[1:])

