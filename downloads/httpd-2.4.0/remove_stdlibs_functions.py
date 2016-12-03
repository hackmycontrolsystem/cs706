import sys
import os

print "******** Cleaning up stdlib functions from cflow output  ********"

functions_filename = open("std_functions_list",'r')
std_funs = set()

for line in functions_filename:
	line = line.strip() 	# Strip the whitespaces
	if line not in std_funs:
		std_funs.add(line)
	else:
		continue

#print "All std funstions list ", std_funs
functions_filename.close()	

input_filename = open("all_cflow","r")
output_filename = open("gdiff_cflow","w")

removed_counter = 0
for line in input_filename:
	#line = line.strip()
	if line[0] == 'm' and line[1] == 'a' and line[2] == 'i' and line[3] == 'n':
		#print line
		line1 = line.split(') <')
		nline = "main() <" + line1[1]
		#print nline
		output_filename.write(nline)
		continue
			

	if line.strip() in std_funs:
		#print line
		removed_counter = removed_counter + 1
		continue
	else:
		output_filename.write(line)

print "Total standard library functions removed: ", removed_counter
input_filename.close()
output_filename.close()
