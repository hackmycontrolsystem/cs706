import xml.etree.ElementTree as ET
import sys

input_filename = 'show_bug.xml'

tree = ET.parse(input_filename)
root = tree.getroot()

#print "Parsing ", root.tag, "and attributes", root.attrib

fwrite = open("bug_id_lists", 'w')

count = 0
for child in root:
	for c in child:
		#print c.tag, #"\t", c.text
		if c.tag == 'bug_id':
			#print c.text
			fwrite.write(c.text)
			fwrite.write('\n')
			count = count + 1
		
		'''
		if c.tag == 'long_desc':
			for d in c:
				print "\t\t", d.tag, "\t", d.text
		'''
		
	#sys.exit()
print "Total bugs: ", count
print "Bug Id list is written in file name: bug_id_lists .", 
fwrite.close()
