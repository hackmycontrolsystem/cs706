import fileinput
import re

#filein = open('test-writev.c', 'r+')
filein = 'test-writev.c'
line_count = 0

for line in fileinput.input(filein, inplace=1, backup='.bak'):
    if line_count == 48:
	line = re.sub('main','bar', line.rstrip())
    print(line)
    line_count = line_count + 1
 
