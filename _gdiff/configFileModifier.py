import os
import sys
from shutil import copyfile

fopen = open('GDiff/config_file.cfg', 'r')
fwrite = open('GDiff/new_config_file.cfg','w')

flag = str(sys.argv[1])

if flag == 'remove':
	for line in fopen:
		if "CFLOW_VERSION2=" in line:
			fwrite.write('CFLOW_VERSION2=None' + '\n')
		else:
			fwrite.write(line)

if flag == 'add':
	for line in fopen:
		if "CFLOW_VERSION2=" in line:
			fwrite.write('CFLOW_VERSION2="/tmp/gdiff/runs/gdiff_cflow_v2"' + '\n')
		else:
			fwrite.write(line)



fwrite.close()
fopen.close()

# Copy config_file.cfg as config_file.cfg.bak
copyfile('GDiff/config_file.cfg','GDiff/config_file.cfg.bak')
copyfile('GDiff/new_config_file.cfg','GDiff/config_file.cfg')
