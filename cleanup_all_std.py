import sys

fopen = open('all_std_functions.txt','r')
fout = open('cleaned_std_functions','w')

c = 0

for line in fopen:
	line = line.strip()
	if ':' in line:
		fout.write(line[:-1] + '()')
		c = c + 1
	else:
		fout.write(line + '()')
		continue

	fout.write('\n')

print c
fopen.close()
fout.close()
