#! /usr/bin/env python3

# Script that renames files based on 3 command-line parameters. Enter:
# - string you want to replace
# - replacement string
# - absolute path or relative path

# 1st checks specific case: Check for filenames in given folder that start
# with _ (underscore) to be replaced by '' (empty string).
# If not that case, then do regular filename replacement.

# --- Example Paths for Testing---
# Command Line:
# '/Users/kimlew/Documents/Courses/Babbel\ Duo\ Ling\ Pims/Swedish'

# PyCharm Params for Testing:
# "_" "" "/Users/kimlew/Documents/Courses/Babbel Duo Ling Pims/Swedish"

# In General: Explicit import best - so you know where import is from.
import sys
from os import rename
from os import walk
from os.path import exists
import pprint


def main():
    # Read in parameters.
    string_to_replace = sys.argv[1]
    replacement_string = sys.argv[2]
    path_of_files = sys.argv[3]

    print('sys.argv[1]: ', string_to_replace)
    print('sys.argv[2]: ', replacement_string)
    print('sys.argv[3]: ', path_of_files)
    print()

    if exists(path_of_files) == False:
        print("This path does NOT exist.")

    if (string_to_replace.startswith("_") and replacement_string == ""):
        # Replace for this special case.
        # Try 1: walk() - yields 2 lists for each directory it visits.
        # Splits into files & dirs for you. If you ONLY want TOP-level
        # directory - break the 1st time it yields.

        print("Doing special case replacement.")
        rename_all_files(string_to_replace, replacement_string,
                         path_of_files)

    else:
        # Replace whatever they wanted replaced with the replacement_string.
        # else - Do straight replacement based on string_to_replace &
        # replacement_string. This should cover cases:  - , _Babbel , etc.
        print("Doing regular replacement.")
        rename_all_files(string_to_replace, replacement_string,
                         path_of_files)


def rename_all_files(string_to_replace, replacement_string, path_of_files):
    print()
    print('IN rename_all_files()')

    filenames_array = []

    # Note:
    # (dirpath, dirnames, filenames)
    # (cur_path, directories, files) in os.walk(directory):
    for (_, _, filenames) in walk(path_of_files):
        print('IN for loop')
        # Test that all files show.
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(filenames)

        filenames_array.extend(filenames)

        # Use replace('_', ''), a string method, startswith() & rename().
        for a_filename in filenames_array:
            print("Path of files is: " + str(path_of_files))
            print("Old filename is: " + str(a_filename))

            if exists(str(path_of_files) + '/' + str(a_filename)) == False:
                print("This file name does NOT exist.")
                break

            new_name = a_filename.replace(string_to_replace,
                                          replacement_string)
            print('New filename is: ', new_name)

            if (a_filename != new_name):
                path_with_old_file = path_of_files + "/" + a_filename
                path_with_new_file = path_of_files + "/" + new_name

                # print("path_with_old_file: " + path_with_old_file)
                # print("path_with_new_file: " + path_with_new_file)

                # rename() - is a top-level function.
                rename(path_with_old_file, path_with_new_file)
    print('')
    print('The filenames have been changed.')


if __name__ == '__main__':
    main()
