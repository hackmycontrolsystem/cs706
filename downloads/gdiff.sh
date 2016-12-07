#!/bin/sh

echo "Parsing and Analyzing folder: "

if [[ $# -gt 2 ]]; then
echo "Usage: bash gdiff.sh <full path to Software v1> [<full path to software v2>]"
echo "More than two argument. Exit..."
exit 0
fi

PATH_V1="$1"
echo "Path to version 1: ${PATH_V1}"

PATH_V2="$2"
echo "Path to version 2: ${PATH_V2}"

mkdir -p /tmp/gdiff/runs
cd ${PATH_V1}

echo "************** Generate ctags ************"
ctags -RV -x --c-types=f ${PATH_V1}/* > /tmp/gdiff/runs/gdiff_tags_v1
echo "ctags generated as file /tmp/gdiff/gdiff_tags_v1"

echo "***************Processing ctags...***********"
python parse_ctags.py /tmp/gdiff/runs/gdiff_tags_v1


#echo "*************** finding all *.c files in project ***********"

#find ./ -type f -name "*.c" > find_output
#echo "all files are listed in find_output file\n"


#echo "*************** Run cflow on all *.c files ***********"
#echo "Running cflow...\n"
#cflow server/*.c modules/aaa/*.c modules/arch/*.c modules/cache/*.c support/*.c os/beos/beosd.c os/bs2000/*.c os/netware/*.c os/os2/*.c os/tpf/*.c os/unix/*.c os/win32/*.c  -o all_cflow

#echo "cflow output at all_cflow file\n"
#python remove_stdlibs_functions.py

#echo "Removed standard library functions from all_flow and result stored in gdiff_cflow\n"

#echo "**************Restoring backups...*********"
#python restore_files_frm_bakup.py 

