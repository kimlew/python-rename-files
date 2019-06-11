#! /usr/bin/env python3

# Script that replaces files in folder that start with _ TO: '' (empty string).
# Enter as command-line parameters:
# 1 - string you want to replace
# 2 - absolute path or relative path

# Path for Testing:
# '/Users/kimlew/Documents/Courses/Babbel\ Duo\ Ling\ Pims/Swedish'
# Params for Testing in PyCharm:
# "_" "" "/Users/kimlew/Documents/Courses/Babbel Duo Ling Pims/Swedish"

# In General: Explicit import best - so you know where import from.
import sys
from os import rename
from os import walk

import os.path
from os import path
from os.path import exists

from os import listdir
from os.path import isfile
from os.path import join

import pprint


def main():
    # Read in parameter with absolute or relative folder path you want.
    string_to_replace = sys.argv[1]
    replacement_string = sys.argv[2]
    path_of_files = sys.argv[3]

    print('sys.argv[1]: ', string_to_replace)
    print('sys.argv[2]: ', replacement_string)
    print('sys.argv[3]: ', path_of_files)
    print("Directory exists: " + str(exists(path_of_files)))
    print()

    # Try 1: walk() - yields 2 lists for each directory it visits.
    # Splits into files & dirs for you. If you ONLY want the TOP-level
    # directory - break the 1st time it yields.

    filenames_array = []

    for (_, _, filenames) in walk(path_of_files):

        # TODO: Add check for if path exists.
        # Use os.path.exists - to check if any directory exists or not.
        # Use os.makedirs - to create a directory.

        if exists(path_of_files) == False:
            print("This path does NOT exist.")
            break

        else:
            # e.g. for path, subdir, files in os.walk(path):
            # e.g. for cur_path, directories, files in os.walk(directory):
            print('Filenames in directory are: ')

            # Test that all files show.
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(filenames)

            filenames_array.extend(filenames)
            print('')

            # Note: Do not need a regex. Use 1 of:
            # rename() OR replace('_', '') OR filename[0] == something
            # Try 2: only_files = [filenames_array for filenames_array in listdir(path_used) if isfile(join(
            # path_used, filenames_array))]


            for a_filename in filenames_array:
                # The '#' is replaced by the '-' in the filenames in the directory.
                # replace() - is a string method.
                # Use startswith().

                print("Path of files is: " + str(path_of_files))
                print("a_filename is: " + str(a_filename))

                if exists(str(path_of_files) + '/' + str(a_filename)) == False:
                    print("This file name does NOT exist.")
                    break

                else:
                    # Rename the file with new_name based on replacement chars.
                    new_name = ''

                    if a_filename.startswith(string_to_replace):
                        new_name = a_filename.replace(string_to_replace, replacement_string)
                        print('new_name is: ', new_name)
                        path_of_files.join(new_name)

                    # if new_name != a_filename:
                    #     # rename() - is a top-level function.
                    #     path_of_files.join(rename(a_filename, new_name))


    # TODO: Add way to rename files if chars to replace are NOT at
    # filename start.

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
