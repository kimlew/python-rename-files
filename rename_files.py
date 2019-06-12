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
from os.path import exists
import pprint


def main():
    # Read in parameter with absolute or relative folder path you want.
    string_to_replace = sys.argv[1]
    replacement_string = sys.argv[2]
    path_of_files = sys.argv[3]

    print('sys.argv[1]: ', string_to_replace)
    print('sys.argv[2]: ', replacement_string)
    print('sys.argv[3]: ', path_of_files)
    print()

    if exists(path_of_files) == False:
        print("This path does NOT exist.")

    else:  # exists(path_of_files) == True:
        # Try 1: walk() - yields 2 lists for each directory it visits.
        # Splits into files & dirs for you. If you ONLY want TOP-level
        # directory - break the 1st time it yields.

        filenames_array = []

        # Note:
        # (dirpath, dirnames, filenames)
        # (path, subdir, files) in os.walk(path):
        # (cur_path, directories, files) in os.walk(directory):
        for (_, _, filenames) in walk(path_of_files):
            print('--- Filenames in directory are: ---')

            # Test that all files show.
            # pp = pprint.PrettyPrinter(indent=4)
            # pp.pprint(filenames)

            filenames_array.extend(filenames)

            # Use: replace('_', ''), then rename(). Do not need a regex.
            # Try 2: only_files = [filenames_array for filenames_array in
            # listdir(path_used) if isfile(join(path_used, filenames_array))]

            for a_filename in filenames_array:
                # replace() - is a string method.
                # Use startswith().

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

    # TODO: Rename file when chars are ANYWHERE in filename, NOT just at start.


# Driver Code
if __name__ == '__main__':
    main()
