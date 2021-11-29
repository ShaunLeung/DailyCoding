# Shaun Leung
# Nov 29, 2021

# This one is labled as hard but it can essentially be boiled down to a tree
# problem. 

# Just knowing file sytems once the string is in a tree form it is trivial to do
# a search and return the path length but it isnt really effecient to go through
#  the whole tree rooting out each file and then comparing.

# you can keep track of the files when building the tree and then return.
# Note that the deepest file does not neccisarily have the longest path. 

# the tricky part will be parsing the string to build the tree... not impossible 
# though. Will be some good practice parsing strings in Python.
# looks like string split will be what I need

# note codes for \t and \n are 0x9 and 0xA respectively

# Changing my mind! not going to go with trees but rather keep track of lengths
# in arrays/dicts! one for dir and one for files. since we know that the 
# preceeding tabs tell us how deep in the file structure we are those correspond 
# to indecies

import re
def longestPath(string):
    # make each dir/file their own element in an array (well not yet but soon)
    string = ''.join(string.split('\n'))
    # split on the tabs so we can count them
    path = re.split('(\t)',string)
    # get rid of empty strings
    path = list(filter(None, path))
    
    files = {}
    # pre-loading to deal with files in root
    dirs = []
    depth = 0
    for item in path:
        if '.' in item:
            files[item] = len(item) + sum(dirs[:depth]) + depth
            depth = 0 # reset depth

        elif item == '\t':
            depth += 1

        else:
            # this will technially overwrite values for dir but we are done with
            # them by now
            if depth < len(dirs):
                dirs[depth] = len(item) # + depth to account for the \s

            # append if new. 
            else: 
                dirs.append(len(item))
            depth = 0 # reset depth

    return max(files.values())


string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(longestPath(string))