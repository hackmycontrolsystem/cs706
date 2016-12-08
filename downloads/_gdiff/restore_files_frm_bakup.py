import re
import sys
import os
import fileinput
from shutil import copyfile

print "*****Starting GDiff Restoring files frm backup script...******\n"

# Read the gdiff_tags file
filename = open(sys.argv[1], 'r')

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
