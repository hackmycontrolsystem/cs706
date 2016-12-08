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


def get_attachments(bug, data):
  """ An html parser only used to get bug attachments """

  soup = BeautifulSoup(data,"lxml")
  table = soup.find("table", id="attachment_table")
  attempts = table.findChildren("tr", {"class":"bz_contenttype_text_plain"})

  for attempt in attempts:
    patch_id = attempt.find('a')['href']
    #loc = http.get("https://bugzilla.mozilla.org/" + patch_id).count('\n')
    #attachment_data = urllib2.urlopen("https://bugzilla.redhat.com/" + patch_id).read()
    attachment_data = urllib2.urlopen("https://bz.apache.org/bugzilla/" + patch_id).read()
    #print "Got attahment", str(attachment_data)
    #print "Got attahment in plain text."

    bug_filename = "bug_db/" + str(get_id(bug)) + ".txt"
    bug_attachment = open(bug_filename, 'w')

    bug_attachment.write(str(attachment_data))
    bug_attachment.close()
    return "Attachment content written in file ", bug_filename


  attempts = table.findChildren("tr", {"class":"bz_contenttype_application_octet-stream"})
  for attempt in attempts:
    patch_id = attempt.find('a')['href']
    return "Attachment not in plain text format. Please parse manually"

  return "No attachment found."


def download(bug):
  #data = http.get(bug)
  data = urllib2.urlopen(bug).read()

  #if "not a valid bug number nor an alias to a bug" in data:
  if "not a valid bug number" in data:
    raise BugNotFound("Bug %s does not exist!" % get_id(bug))

  soup = BeautifulSoup(data,'html.parser')
  #print soup.prettify()
  status = soup.find('span', attrs={'id':'static_bug_status'})
  status = status.text
  status = status.replace('\n','')
  print "Status of Bug",get_id(bug),":",  status

  return get_attachments(bug, data)

