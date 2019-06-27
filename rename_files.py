#! /usr/bin/env python3

# Script that renames files based on 3 command-line parameters. Enter:
# - string you want to replace
# - replacement string
# - absolute path or relative path

# --- Example Paths for Testing---
# Command Line: python3 rename_files.py "_Babble Spanish" ""
# "/Users/kimlew/Documents/Courses/Babbel\ Duo\ Ling\ Pims/Swedish"

# PyCharm Params for Testing:
# "_" "" "/Users/kimlew/Documents/Courses/Babbel Duo Ling Pims/Swedish"

# Best Practice: Explicit import - so you know where import is from.
import sys
from os import rename
from os import walk
from os.path import exists


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

    else:
        print("Doing replacement.")
        rename_all_files(string_to_replace, replacement_string,
                         path_of_files)


def rename_all_files(string_to_replace, replacement_string, path_of_files):
    filenames_array = []

    # Note:
    # (dirpath, dirnames, filenames)
    # (cur_path, directories, files) in os.walk(directory):
    for (_, _, filenames) in walk(path_of_files):
        filenames_array.extend(filenames)

        # Use replace('_', ''), a string method, startswith() & rename().
        for a_filename in filenames_array:
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
