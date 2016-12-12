# Script to collect all functions in call trace of abrt 
# Then it parses and removes functions that are not present in trace from cflow output
import re
import sys
import os
import fileinput
from shutil import copyfile

if len(sys.argv) != 3:
	print "Usage: python parse_abrt.py <result.txt> <ctags file>"
	sys.exit(0)

# Read the stack trace file
filename = open(sys.argv[1], 'r')

# Dictionary: {bug_id: set of all functions stack trace}
bugdict = {}

# File format:  bug_id: fn()#fn1()...
for line in filename:
	line = line.strip()
	line = line.split(': ')
	#print line[0], "\t", line[1]
	if line[0] not in bugdict:
		bugdict[line[0]] = line[1]

filename.close()
#print bugdict

functions_list = {}

for bug in bugdict:
	trace = bugdict[bug]
	trace = trace.split('#')[1:3]
	for fn in trace:
		if fn not in functions_list:
			functions_list[fn] = ""
		else:
			continue
		
#print functions_list	

#Open cflow files which are given as inputs and modify them to generate cflow with 
# functions that are present in call traces.

fctags = open(sys.argv[2], 'r')
all_files = set()

x = 0
for line in fctags:
	#x = x + 1
	#if x > 10:
#		sys.exit(0)
	line = line.strip()
	line = line.split()
	func_name = line[0]
	if func_name in functions_list:
		functions_list[func_name] = line[3]
		all_files.add(line[3])
		#print line[0], line[3]

#print " ******************************************************\n\n"
#print functions_list

print ' '.join(str(x) for x in all_files)

#for files in all_files:
#	print files
#print all_files


