#! /usr/bin/env python3

# Script that replaces files in folder that start with _ TO: '' (empty string).
# Enter as command-line parameter:
# 1 - string you want to replace
# 2 - absolute path or relative path

# In General: Explicit import best - so you know where import from.
import sys
import os

from os import walk
from os import listdir
from os.path import isfile
from os.path import join

import pprint


def main():
    # Read in parameter with absolute or relative folder path you want.

    string_to_replace = sys.argv[1]
    path_of_files = sys.argv[2]
    print('sys.argv[1]: ', string_to_replace)
    print('sys.argv[2]: ', path_of_files)
    print()

    # Intialized path for testing.
    '''
    path_name = '/Users/kimlew/Documents/Courses/Babbel\ Duo\ Ling\ Pims/Swedish'
    '''

    # Try 1: walk() - yields 2 lists for each directory it visits - splits
    # into files & dirs for you. If you ONLY want the TOP-level directory -
    # break the 1st time it yields.
    filenames_array = []
    for (_, _, filenames) in walk(path_of_files):
        # e.g. for path, subdir, files in os.walk(path):
        # e.g. for cur_path, directories, files in os.walk(directory):
        print('Filenames are: ')

        # Test that all files show.
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(filenames)

        filenames_array.extend(filenames)
        print('')

        # TODO: Use 1 of:
        # rename()
        # replace('_', '')
        # starts_with()

        for a_filename in filenames_array:
            # The '#' is replaced by the '-' in the filenames in the directory.
            new_name = a_filename.replace('_', '')
            print('new_name is: ', new_name)

            if new_name != a_filename:
                os.rename(a_filename, new_name)

        # Note: Do not need a regex.
        # Use to find if filename starts: filename[0] ==

        # Try 2: only_files = [filenames_array for filenames_array in listdir(path_used) if isfile(join(
        # path_used, filenames_array))]

    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(filenames_array)

# -- Helpful Info --
'''
# Loop through every file in the current working directory.
print("os.listdir('.') is: ", os.listdir('.'))
print()

for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue    # Skip non-csv files.
'''
# os.path.getsize('/tmp')

# for filename in myFiles:
# ...         print(os.path.join('/users/kim', filename))
#     os.getcwd()

# Driver Code
if __name__ == '__main__':
    main()
