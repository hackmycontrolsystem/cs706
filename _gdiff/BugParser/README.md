Bugzilla-py
===========

This is an experimental library used to crawl meta-data information of bugs reports at [Bugzilla](http://bugzilla.mozilla.org/).

Usage: Command line
-------------------

If you want to crawl a sigle bug report, use

```
python bugzilla.py -b <bug-id>
```

Or, if you have a list of bugs reports, you might want to use

```
python bugzilla.py -l <file>
```

Where file is a .txt file with one bug report id per line. The results are saved in a csv file named ``output.csv`` in the root dir.

Use --help to see all options.


Usage: Source code
------------------

Download the source code

```
git clone git@github.com:rgodha/cs706.git
```

Requirements
------------

* python 2.7 or above
* BeautifulSoup
* urllib2
