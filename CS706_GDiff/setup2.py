import os
import sys
import datetime

from cx_Freeze import setup, Executable
from numpy.f2py.cfuncs import includes

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
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['jinja2', 'jinja2.ext','flask_sqlalchemy','flask', 'flask_login', 'os', 
                                'flask_wtf','flask_sqlalchemy._compat','sqlalchemy.dialects.sqlite',
                           'sqlalchemy'], 
                    include_files = includefiles, 
                    include_msvcr = True, 
                    includes = [ 'jinja2', 'jinja2.ext','atexit'], 
                    excludes = ['tcl',
               'Tkconstants', 'Tkinter'])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None
#base=None

dt = datetime.datetime.now()

executables = [
    Executable('/Users/mehreenali/Documents/workspace/GDiff/runserver.py', base=base, targetName = 'GDiff')
]
main_executable = Executable("/Users/mehreenali/Documents/workspace/GDiff/runserver.py", base=base, targetName = 'GDiff', compress = True,
    copyDependentFiles = True,
    appendScriptToExe = False,
    appendScriptToLibrary = False,
    icon = None)

setup(name ='GDiff',
      version = '1.0' + dt.strftime('%m%d.%H%m'),
      author = 'Mehreen',
      author_email = 'mali24@wisc.edu',
      description = 'GDiff',
      compress = True,
      copyDependentFiles = True,
      appendScriptToExe = False,
      appendScriptToLibrary = False,
      icon = None,
      options = dict(build_exe = buildOptions),
      executables = [main_executable], requires=['flask', 'wtforms']#,
      #install_requires=[
       # 'Flask==0.10.1',
       # 'SQLAlchemy==1.0.8'
    #]
      )

