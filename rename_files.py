#! /usr/bin/env python3

# Script that replaces files in folder that start with _ TO: '' (empty string).
# Enter absolute path or relative path as command-line parameter.

from os import walk # In General: Explicit best - so you know where import from.
import pprint

# Read in parameter with absolute or relative folder path you want.

 # Intialize mypath.
path_used = '/Users/kimlew/Documents/Courses and Tutorials/_aFRENCH_Spanish_Swedish/Swedish Babbel'

f = []
for (_, _, filenames) in walk(path_used):
    print('Filenames are: ')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(filenames)

    f.extend(filenames)

# Helpful info:
# os.path.getsize('/tmp')
# pprint

#for filename in myFiles:
#...         print(os.path.join('/users/kim', filename))
# os.getcwd()
