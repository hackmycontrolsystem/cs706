#!/bin/sh

echo "Parsing and Analyzing folder: "

if [[ $# -gt 1 ]]; then
echo "Usage: bash gdiff.sh <path to Software>"
echo "More than one argument. Exit..."
exit 0
fi

APP_PATH="$1"
echo "${APP_PATH}"


echo "************** Generate ctags ************"
ctags -RV -x --c-types=f * > gdiff_tags
echo "ctags generated as file gdiff_tags_v1\n"

echo "***************Processing ctags...***********"
python parse_ctags.py


echo "*************** finding all *.c files in project ***********"

find ./ -type f -name "*.c" > find_output
echo "all files are listed in find_output file\n"


echo "*************** Run cflow on all *.c files ***********"
echo "Running cflow...\n"
cflow server/*.c modules/aaa/*.c modules/arch/*.c modules/cache/*.c support/*.c os/beos/beosd.c os/bs2000/*.c os/netware/*.c os/os2/*.c os/tpf/*.c os/unix/*.c os/win32/*.c  -o all_cflow

echo "cflow output at all_cflow file\n"
python remove_stdlibs_functions.py

echo "Removed standard library functions from all_flow and result stored in gdiff_cflow\n"

echo "**************Restoring backups...*********"
python restore_files_frm_bakup.py 
