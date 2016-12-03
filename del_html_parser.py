import os
import re
import sys

html_file = open('Function-Index.html','r')
c = 0

line = '<tr><td></td><td valign="top"><a href="Termination-Internals.html#index-_005fexit"><code>_exit</code></a>:</td><td>&nbsp;</td><td valign="top"><a href="Termina tion-Internals.html#Termination-Internals">Termination Internals</a></td></tr>'

if "<code>" in line:
	fname = re.match( r'code (.*?) ', line)
	print fname


'''
for line in html_file:
	if "<code>" in line:
		fname = re.m
		c = c + 1
'''
print "Total count ", c
html_file.close()
