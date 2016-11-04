# Parse the ctags: 
#	1. Extract all files that contain main() function call

import re
import sys
import os
import fileinput
from shutil import copyfile

print "*****Starting GDiff Parsing ctags script...******\n"

# Read the gdiff_tags file
filename = open("gdiff_tags", 'r')

# Files that contain main functions
# Dictionary: {filename: line_number for main()}
main_filelist = {}

# main should be first symbol in the line
#print "Funtion Name\t File Name\t Line No"
for line in filename:
	line = line.split()
	if line[0] == "main":
		#print line[0], "\t", line[3], "\t", line[2]
		main_filelist[line[3]] = line[2]

filename.close()
#print main_filelist

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

### Run cflow and get results 


## Again copy back the .bak files to original files

#c = 1
for main_file in main_filelist:
#	if c > 1:
#		sys.exit()

	main_file_location = main_file				## file location
	main_file_location_bak = main_file_location + ".bak"

	copyfile(main_file_location_bak, main_file_location)
	print "Restored file", main_file_location_bak, "to ", main_file_location, "and deleted bakup file"	
	os.remove(main_file_location_bak)
	#print "Deleted the backup copy"
#	c = c+1


