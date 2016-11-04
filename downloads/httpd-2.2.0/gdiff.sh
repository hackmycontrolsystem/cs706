#!/bin/sh

echo "***************Parsing ctags...***********"
python parse_ctags.py


echo "**************Restoring backups...*********"
python restore_files_frm_bakup.py 
