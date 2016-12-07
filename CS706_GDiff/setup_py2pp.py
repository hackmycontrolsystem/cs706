"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import os
import sys
import datetime
from setuptools import setup

def files_under_dir(dir_name):
    file_list = []
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            file_list.append(os.path.join(root, name))
    return file_list

includefiles = []
for directory in ('GDiff/static', 'GDiff/templates',  'input', 'output', 'GDiff', 'static', 'templates','models', 'GDiff/models'):
    includefiles.extend(files_under_dir(directory))

print "included files", includefiles

APP = ['runserver.py']
DATA_FILES = includefiles
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
