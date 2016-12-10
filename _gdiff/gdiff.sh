#!/bin/sh
# Shell Script for running the GDiff Tool

#echo "Parsing and Analyzing folder: "

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


echo "************** Generate ctags ************"
ctags -RV -x --c-types=f ${PATH_V1}/* > /tmp/gdiff/runs/gdiff_tags_v1
echo "ctags generated as file /tmp/gdiff/runs/gdiff_tags_v1"


echo "************** Processing ctags...***********"
python parse_ctags.py /tmp/gdiff/runs/gdiff_tags_v1


echo "************ finding all *.c files in project ***********"
C_FILES=$(find ${PATH_V1}/* -type f -name "*.c") # > /tmp/gdiff/runs/find_output_v1
echo "all files are listed in /tmp/gdiff/runs/find_output file\n"

SAVE_CWD=$PWD
echo "*************** Run cflow on all *.c files ***********"
echo "Running cflow..."
cd ${PATH_V1}

#cflow server/*.c server/mpm/event/*.c server/mpm/worker/*.c server/mpm/netware/*.c server/mpm/prefork/*.c server/mpm/winnt/*.c server/mpm/mpmt_os2/*.c  modules/aaa/*.c modules/arch/*.c modules/cache/*.c support/*.c os/beos/beosd.c os/bs2000/*.c os/netware/*.c os/os2/*.c os/tpf/*.c os/unix/*.c os/win32/*.c  -o /tmp/gdiff/runs/all_cflow
echo $C_FILES

cflow $C_FILES -o /tmp/gdiff/runs/all_cflow
#cflow inode.c namei.c locks.c read_write.c -o /tmp/gdiff/runs/all_cflow
#cflow inode.c  -o /tmp/gdiff/runs/all_cflow
echo " " >> /tmp/gdiff/runs/all_cflow

cd $SAVE_CWD

echo "cflow output at  /tmp/gdiff/runs/all_cflow file\n"
python remove_stdlibs_functions.py /tmp/gdiff/runs/all_cflow /tmp/gdiff/runs/gdiff_cflow_v1

echo "Removed standard library functions from all_flow and result stored in gdiff_cflow\n"

echo "**************Restoring backups...*********"
python restore_files_frm_bakup.py /tmp/gdiff/runs/gdiff_tags_v1 

exit 0



echo " *********** Run for ver2 ********** "
if [[ $2 == *"NULL"* ]]; then
echo "Version 2 not present. Exit.."
exit 0
fi

echo "************** Generate ctags ************"
ctags -RV -x --c-types=f ${PATH_V2}/* > /tmp/gdiff/runs/gdiff_tags_v2
echo "ctags generated as file /tmp/gdiff/runs/gdiff_tags_v2"


echo "************** Processing ctags...***********"
python parse_ctags.py /tmp/gdiff/runs/gdiff_tags_v2


echo "************ finding all *.c files in project ***********"
find ${PATH_V2}/* -type f -name "*.c" > /tmp/gdiff/runs/find_output_v2
echo "all files are listed in /tmp/gdiff/runs/find_output_v2 file\n"

SAVE_CWD=$PWD
echo "*************** Run cflow on all *.c files ***********"
echo "Running cflow..."
cd ${PATH_V2}

#cflow server/*.c server/mpm/event/*.c server/mpm/worker/*.c server/mpm/netware/*.c server/mpm/prefork/*.c server/mpm/winnt/*.c server/mpm/mpmt_os2/*.c  modules/aaa/*.c modules/arch/*.c modules/cache/*.c support/*.c os/beos/beosd.c os/bs2000/*.c os/netware/*.c os/os2/*.c os/tpf/*.c os/unix/*.c os/win32/*.c  -o /tmp/gdiff/runs/all_cflow2

cflow bufferv2.c -o /tmp/gdiff/runs/all_cflow2
#cflow inode.c namei.c locks.c read_write.c -o /tmp/gdiff/runs/all_cflow2
#cflow inode.c  -o /tmp/gdiff/runs/all_cflow2
echo " " >> /tmp/gdiff/runs/all_cflow2

cd $SAVE_CWD

echo "cflow output at  /tmp/gdiff/runs/all_cflow2 file"
python remove_stdlibs_functions.py /tmp/gdiff/runs/all_cflow2 /tmp/gdiff/runs/gdiff_cflow_v2

echo "Removed standard library functions from all_flow and result stored in gdiff_cflow2\n"

echo "**************Restoring backups...*********"
python restore_files_frm_bakup.py /tmp/gdiff/runs/gdiff_tags_v2
python runserver.py
