# -*- coding: utf-8 -*-

import codecs
import re, os
import sys
from bs4 import BeautifulSoup
import urllib2

class BugNotFound(Exception):
  def __init__(self, message):
    Exception.__init__(self, message)

def get_id(bug_url):
  return bug_url.split("=")[1]


def get_attachments(data):
  """ An html parser only used to get bug attachments """

  soup = BeautifulSoup(data,"lxml")
  table = soup.find("table", id="attachment_table")
  attempts = table.findChildren("tr", {"class":"bz_contenttype_text_plain"})

  #loc_per_attempt = []

  for attempt in attempts:
    patch_id = attempt.find('a')['href']
    print " ## Rahul ## ", patch_id
    #loc = http.get("https://bugzilla.mozilla.org/" + patch_id).count('\n')
    attachment_data = urllib2.urlopen("https://bugzilla.redhat.com/" + patch_id).read()
    print "Got attahment", str(attachment_data)
    attachment_data = str(attachment_data)
    #loc_per_attempt.append(str(loc))

  #return Attachment(len(attempts), loc_per_attempt)
  return attachment_data


def download(bug):
  #data = http.get(bug)
  print " #### Rahul #### ", bug
  data = urllib2.urlopen(bug).read()

  #if "not a valid bug number nor an alias to a bug" in data:
  if "not a valid bug number" in data:
    raise BugNotFound("Bug %s does not exist!" % get_id(bug))

  soup = BeautifulSoup(data,'html.parser')
  #print soup.prettify()
  status = soup.find('span', attrs={'id':'static_bug_status'})
  status = status.text
  status = status.replace('\n','')
  print status



  attachment = get_attachments(data)
  print attachment
  #status = get_element(data, "id=\"static_bug_status\">", "<")

