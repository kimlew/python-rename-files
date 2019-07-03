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
    string_to_replace, replacement_string, starting_dir = get_input()

    if exists(starting_dir) is False:
        print("This path does NOT exist.")

    else:
        print("Doing replacement...")
        rename_all_files(string_to_replace, replacement_string, starting_dir)
        print()


def get_input():
    print(" You entered", len(sys.argv)-1, "arguments at the command line.")

    if len(sys.argv) != 4:
        # Ordinary exception now vs. IndexError: list index out of range.
        raise Exception(
            " Error: Wrong number of arguments. Enter 3 arguments: 1. "
            "string to replace 2. replacement string 3. path for files ")

    # Read in parameters.
    string_to_replace = sys.argv[1]
    replacement_string = sys.argv[2]
    starting_dir = sys.argv[3]

    print(' String to replace:\t', string_to_replace)
    print(' Replacement string:\t', replacement_string)
    print(' Folder path:', starting_dir)
    print()
    return string_to_replace, replacement_string, starting_dir


def rename_all_files(string_to_replace, replacement_string, starting_dir):
    files_changed_count = 0

    # Note:
    # (dirpath, dirnames, filenames) in os.walk(directory)
    # (cur_path, directories, files) in os.walk(directory)
    # Note: dirpath
    # - ensures that path with sub-directories is used, if applicable
    # - is the start location for each iteration - varies since it changes if
    # there are sub-directories
    # - is the 1st part of each directory-path-files tuple
    for (dirpath, _, filenames) in walk(starting_dir):

        for a_filename in filenames:
            if exists(str(dirpath) + '/' + str(a_filename)) is False:
                print("This file name does NOT exist.")
                break

            new_name = a_filename.replace(string_to_replace,
                                          replacement_string)

            if a_filename != new_name:
                print("Old filename is: " + str(a_filename))
                print('New filename is:', new_name)

                path_with_old_file = dirpath + "/" + a_filename
                path_with_new_file = dirpath + "/" + new_name

                # Note: rename() - is a top-level function.
                rename(path_with_old_file, path_with_new_file)
                files_changed_count = files_changed_count + 1
    print()
    print('Renamed: ', files_changed_count, ' file(s)')


if __name__ == '__main__':
    main()
