import sys, os
import mycrawler
import argparse
from reporting import report
import time
import xml.etree.ElementTree as ET

ARGS = argparse.ArgumentParser(description="Bugzilla web crawler")

ARGS.add_argument('-b', nargs=1, help='A bug id')
ARGS.add_argument('-f', nargs=1, help='Uses a file with a list of bugs id')
ARGS.add_argument('-x', nargs=1, help='XML file, downloaded from bugzilla')


def fix_url(url):
  """Prefix a schema-less URL with http://."""
  if '://' not in url:
    #url = 'https://bugzilla.mozilla.org/show_bug.cgi?id=' + url
    url = 'https://bugzilla.redhat.com/show_bug.cgi?id=' + url
    #url = 'https://bz.apache.org/bugzilla/show_bug.cgi?id=' + url
  return url.replace("\n", "")


def read(file):
  """ Read from a file. Returns a list of strings """

  try:
    f = open(file, "r")
  except IOError, e:
    print "No such file or directory: '%s'" % file
    sys.exit(0)

  lines = f.readlines()
  f.close()
  return lines


def parse_xml_bugs(input_filename):
  print "Reading XML fle and get list of all bugs", input_filename

  tree = ET.parse(input_filename)
  root = tree.getroot()
  bugs_list = []

  count = 0
  for child in root:
    for c in child:
      if c.tag == 'bug_id':
        bugs_list.append(c.text)
        count = count + 1

  print "Total bugs: ", count

  bugs = [fix_url(bug) for bug in bugs_list]
  return bugs


def main():
  """ Main program.
  Parse arguments, run crawler, print report
  """
  args = ARGS.parse_args()
  if not args.b and not args.f and not args.x:
    print "Use --help for command line help"
    return

  if args.b:
    bugs = {fix_url(bug) for bug in args.b}
  elif args.f:
    bugs = [fix_url(bug) for bug in read(args.f[0])]
  elif args.x:
    bugs = parse_xml_bugs(args.x[0])
  else:
    print "Use --help for command line help"
    return 

  ## Create a folder to save bug details
  filename = "bug_db/tmp.txt"
  if not os.path.exists(os.path.dirname(filename)):
    try:
      os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
      if exc.errno != errno.EEXIST:
        raise
  
  try:
    output = []
    start_time = time.time()

    for bug in bugs:
      result = mycrawler.download(bug)
      output.append(result)
      print result

    total_time = round(time.time() - start_time, 2)
    print "It took %s seconds to download %s bug reports!" % (total_time, len(bugs))

    #report(output)
  except KeyboardInterrupt:
    print "Interupted!"
  except mycrawler.BugNotFound, e:
    print "An error occurred while crawling bug: " + bug
    print e.message
  except:
    print "An error occurred while crawling bug: " + bug
    raise


if __name__ == "__main__":
  main()
