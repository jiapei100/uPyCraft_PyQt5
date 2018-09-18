from distutils.core import setup
# import py2exe
import sys


#this allows to run it with a simple double click.
# sys.argv.append('py2exe')

py2exe_options = {
        "includes": ["sip","PyQt5.QtCore","PyQt5.QtGui"],
        "dll_excludes": ["MSVCP90.dll"],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 0,
        }

setup(
      name = 'IDE',
      version = '1.1',
      windows = [{"script":'uPyCraft.py',
                  "icon_resources": [(1,"./images/logo.ico")]
                }], 
      zipfile = None,
      
#       options = {'py2exe': py2exe_options}
      )