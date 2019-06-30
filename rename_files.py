#! /usr/bin/env python3

# Script for use on local machine that renames files based on 3
# command-line parameters. Enter:
# - string you want to replace
# - replacement string
# - absolute path or relative path

# --- Example Paths for Testing---
# Command Line: python3 rename_files.py "_Babble Spanish" ""
# "/Users/kimlew/Documents/Courses/Babbel\ Duo\ Ling\ Pims/Spanish"

# PyCharm Params for Testing:
# "_" "" "/Users/kimlew/Documents/Courses/Babbel Duo Ling Pims/Swedish"

# Best Practice: Explicit import - so you know where import is from.
import sys
from os import rename
from os import walk
from os.path import exists


def main():
    string_to_replace, replacement_string, path_of_files = get_input()

    if exists(path_of_files) is False:
        print("This path does NOT exist.")

    else:
        print("Doing replacement...")
        rename_all_files(string_to_replace, replacement_string, path_of_files)
        print()


def get_input():
    # Read in parameters.
    string_to_replace = sys.argv[1]
    replacement_string = sys.argv[2]
    path_of_files = sys.argv[3]

    print('String to replace: ', string_to_replace)
    print('Replacement string: ', replacement_string)
    print('Folder path: ', path_of_files)
    print()
    return string_to_replace, replacement_string, path_of_files


def rename_all_files(string_to_replace, replacement_string, path_of_files):
    filenames_array = []
    files_changed_count = 0

    # Note:
    # (dirpath, dirnames, filenames)
    # (cur_path, directories, files) in os.walk(directory):
    for (_, _, filenames) in walk(path_of_files):
        filenames_array.extend(filenames)

        for a_filename in filenames_array:
            if exists(str(path_of_files) + '/' + str(a_filename)) is False:
                print("This file name does NOT exist.")
                break

            new_name = a_filename.replace(string_to_replace,
                                          replacement_string)

            if a_filename != new_name:
                print("Old filename is: " + str(a_filename))
                print('New filename is:', new_name)

                path_with_old_file = path_of_files + "/" + a_filename
                path_with_new_file = path_of_files + "/" + new_name

                # Note: rename() - is a top-level function.
                rename(path_with_old_file, path_with_new_file)
                files_changed_count = files_changed_count + 1
    print()
    print('Renamed: ', files_changed_count, ' file(s)')


if __name__ == '__main__':
    main()
