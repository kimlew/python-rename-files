#! /usr/bin/env python3

# Script that replaces files in folder that start with _ TO: '' (empty string).
# Enter absolute path or relative path as command-line parameter.

# In General: Explicit import best - so you know where import from.
from os import walk
import pprint


def main():
    # Read in parameter with absolute or relative folder path you want.
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


# Helpful Info:
# os.path.getsize('/tmp')

# for filename in myFiles:
# ...         print(os.path.join('/users/kim', filename))
#     os.getcwd()

# Driver Code
if __name__ == '__main__':
    main()
