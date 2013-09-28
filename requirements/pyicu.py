from distutils.sysconfig import get_python_lib
from shutil import copyfile
import os

destination_dir = get_python_lib()
source_dir = '/usr/lib/python2.7/dist-packages'
target_files = ['_icu.so', 'icu.pyc', 'docs.pyc', 'PyICU.pyc']

for tf in target_files:
    copyfile(os.path.join(source_dir, tf), os.path.join(destination_dir, tf))
