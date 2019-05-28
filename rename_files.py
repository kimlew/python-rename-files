#! /usr/bin/env python3

# Script that replaces files in folder that start with _ TO: '' (empty string).
# Enter as command-line parameter:
# 1 - string you want to replace
# 2 - absolute path or relative path

# In General: Explicit import best - so you know where import from.
import sys
from os import walk
import pprint


def main():
    # Read in parameter with absolute or relative folder path you want.

    string_to_replace = sys.argv[1]
    path_of_files = sys.argv[2]
    print('sys.argv[1]: ', string_to_replace)
    print('sys.argv[2]: ', path_of_files)
    print()

    # Intialized path for testing.
    path_used = '/Users/kimlew/Documents/Courses and ' \
                'Tutorials/_aFRENCH_Spanish_Swedish/Swedish Babbel/'

    f = []
    for (_, _, filenames) in walk(path_used):
        print('Filenames are: ')
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(filenames)

        f.extend(filenames)
        print('')

        # Do not need a regex. Use: filename[0] == '_'
        # rename()
        # replace('_', '')


# Helpful Info:
# os.path.getsize('/tmp')

# for filename in myFiles:
# ...         print(os.path.join('/users/kim', filename))
#     os.getcwd()

# Driver Code
if __name__ == '__main__':
    main()
