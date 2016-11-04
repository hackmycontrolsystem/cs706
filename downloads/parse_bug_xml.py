import xml.etree.ElementTree as ET
import sys

input_filename = 'show_bug.xml'

tree = ET.parse(input_filename)
root = tree.getroot()

print "Parsing ", root.tag, "and attributes", root.attrib

for child in root:
	for c in child:
		print c.tag, "\t", c.text
		
		if c.tag == 'long_desc':
			for d in c:
				print "\t\t", d.tag, "\t", d.text
		
	sys.exit()
