#! /usr/bin/env python3

# Script that replaces files in folder that start with a specific char.
# e.g. _ (underscore) to '' (empty string).
# Enter 3 command-line parameters:
# 1 - string you want to replace
# 2 - replacement string
# 3 - absolute path or relative path

# Path for Testing:
# '/Users/kimlew/Documents/Courses/Babbel\ Duo\ Ling\ Pims/Swedish'
# Params for Testing in PyCharm:
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

        filenames_array = []

        # Note:
        # (dirpath, dirnames, filenames)
        # (cur_path, directories, files) in os.walk(directory):
        for (_, _, filenames) in walk(path_of_files):
            print('--- Filenames in directory are: ---')

            # Test that all files show.
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(filenames)

            filenames_array.extend(filenames)

            # Use replace('_', ''), a string method, startswith() & rename().
            for a_filename in filenames_array:

                print("Path of files is: " + str(path_of_files))
                print("a_filename is: " + str(a_filename))

                if exists(str(path_of_files) + '/' + str(a_filename)) == False:
                    print("This file name does NOT exist.")
                    break

                else:
                    # Rename the file with new_name based on replacement chars.
                    print('Does a_filename start with ' + string_to_replace +
                          ": " + str(a_filename.startswith(string_to_replace)))
                    print('')

                    if a_filename.startswith(string_to_replace) == True:
                        new_name = a_filename.replace(string_to_replace,
                            replacement_string)
                        print('new_name is: ', new_name)

                        path_with_old_file = path_of_files + "/" + a_filename
                        path_with_new_file = path_of_files + "/" + new_name

                        print("path_with_old_file: " + path_with_old_file)
                        print("path_with_new_file: " + path_with_new_file)

                        # rename() - is a top-level function.
                        rename(path_with_old_file, path_with_new_file)

    else:
        # Replace whatever they wanted replaced with the replacement_string.
        # else - Do straight replacement based on string_to_replace &
        # replacement_string. This should cover cases:  - , _Babbel , etc.
        print("Doing regular replacement.s")

    print('The filenames have been changed.')


if __name__ == '__main__':
    main()
