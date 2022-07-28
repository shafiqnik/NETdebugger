'''
from command line goto the folder where all python scripts are located
then run the following command python setup.py py2exe

'''
import glob
import os
from distutils.core import setup

import babel
import py2exe
import sys

file_path=os.path.realpath(__file__)
print('path is ',file_path)


if hasattr( sys, 'frozen' ):
    _dirname = os.path.join(os.path.dirname(sys.executable), 'localedata')
else:
    _dirname = os.path.join(os.path.dirname(__file__), 'localedata')


#data_files = [( "localedata", glob.glob( os.path.join( os.path.dirname( babel.__file__ ), "localedata" ))]


