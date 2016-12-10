GDiff - A Graphical Call Graph Diff Visualizer
===============================================

This is a class project for [CS706](https://www.cs.wisc.edu/courses/706) at University of Wisconsin, Madison with [Prof. Ben Liblit](http://pages.cs.wisc.edu/~liblit/).

Summary 
-------
GDiff is a tool that generates call graph diff of two software versions using modern interactive visualizations techniques D3 (Data-Driven Documents). GFlow takes as input two sets of software artifacts. The first artifact is a pair of software versions written in C language and the second artifact is the bug repository associated with the software. It processes and analyzes both the artifacts to produce a call graph that highlights the paths that were added/deleted between the two version releases. It will also associate paths within the generated call graph with the corresponding bug IDs.

Usage: Command line
-------------------
Run the gdiff tool as: 
```
bash gdiff.sh <path to software ver1> <path to software ver2>
```

Where path to software version 1 is absolute path to your folder containing the version of the software that you need to analyse. Similarly, path to software version 2 is absolute path for different version of the same software. If there is no other version or you just want to analyse the 1st version only, then you should specify NULL as the second argument. If you specify the second version, it should be a later version of the same software.
Example command line usage when both software versions need to be compared:
```
bash gdiff.sh /tmp/gdiff/test_v1/ /tmp/gdiff/test_v2/
```
Example command line usage when you just have 1st version to analyse:
```
bash gdiff.sh /tmp/gdiff/test_v1/ NULL
```

Usage: Source Code
-------------------
```
git clone git@github.com:rgodha/cs706.git
```
Go to the 'gdiff' folder, run the gdiff shell script as specified the examples explained above in command line usage. The tool creates files in /tmp/gdiff/runs folder. Please make sure that the tool has access to /tmp/ folder and has required privileges to create files and folder in /tmp directory.

Requirements
-------------

* python 2.7 or 2.10
* BeautifulSoup
* urllib2
* ctags
* cflow

