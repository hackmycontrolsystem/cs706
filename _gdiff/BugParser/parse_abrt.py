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
print bugdict

functions_list = {}

for bug in bugdict:
	trace = bugdict[bug]
	trace = trace.split('#')
	for fn in trace:
		if fn not in functions_list:
			functions_list[fn] = ""
		else:
			continue
		
print functions_list	

#Open cflow files which are given as inputs and modify them to generate cflow with 
# functions that are present in call traces.

fctags = open(sys.argv[2], 'r')
all_files = []

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
		all_files.append(line[3])
		print line[0], line[3]

print " ******************************************************\n\n"
print functions_list
print all_files


'''
# If only 1 file that contain main() in whole application
# We do not need to rename main, 
# Directly run cflow
if len(main_filelist) <= 1:
	print "Only 1 main() in application. Run cflow. exit() for now."
	sys.exit()


# If there are more than 1 main() funtion in the software application then
# 	for all files in main_filelist, modify main() to main_filename
#c = 1
for main_file in main_filelist:
#	if c > 1:
#		continue

	# Get main_file_name location and main_file_value
	main_file_location = main_file				## file location
	main_file_value = main_filelist[main_file]		## line with main() function in file

	## file_location is of form " /server/os/main.c" 
	## Get the filename as main.c to append to main() 
	main_file_location_split = main_file_location.split('/')
	main_file_name = ""

	if len(main_file_location_split) > 1:
		main_file_name = main_file_location_split[len(main_file_location_split) - 1]
	else:
		main_file_name = main_file_location_split[0]
	
	print "Prepare to modify main() in", main_file_name, "at location", main_file_location, main_file_value
	main_file_name = main_file_name[:-2]			## Remove '.c' from the file name


	## Create a backup of file 
	#main_file_location_bkup = main_file_location + "_bkup"
	#copyfile(main_file_location, main_file_location_bkup)
	print "Backup of " + main_file_location + " is created as " + main_file_location + ".bak"
	new_name = "main_" + main_file_name

	line_count = 0
	for line in fileinput.input(main_file_location, inplace=1, backup='.bak'):
		if line_count == int(main_file_value) - 1:
	    		line = re.sub('main',new_name, line.rstrip())
			print line
		else:
			print line,
		line_count = line_count + 1

	print "main is modified to ", new_name, "at", main_file_location, main_file_value, "\n"
#	c = c+1
'''

