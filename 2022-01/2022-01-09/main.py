# Shaun Leung
# Jan 9, 2022

"""
This one was a little confusing. I had to look up some hints just because rotated an unknown number of times is essentially unsorting the list. 
Essentially what need to be done is that you need to divide and conquer to 
get a nice O(logN) time which is faster than O(N).

The hint I looked up was if the the array was only rotated once. 
"""


def bSearch(array, x):
    """
    Simple funtion that returns the index of item x in the array. Note that the
    array must be sorted for this to work.

    :Param array: Array to be searched
    :Param x" Item to be found in the array
    "Return: The index of X in the array, None if it is not in the array
    """

    n = len(array)
    if n == 1:
        if array[0] == x:
            return 0
        else:
            return None  # x isnt in the list

    # split the array
    left = array[:n//2]
    right = array[n//2:]
    if left[0] <= x and x <= left[-1]:
        index = bSearch(left, x)
        if index != None:
            return index
    else:
        index = bSearch(right, x)
        if index != None:
            return len(left) + index

    # a None bubbled up
    return None


# bsearch test
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if bSearch(array, 5) != 5:
    print("bSearch error")


def shuffleSearch(array, x):
    """
    Similar function to bSearch but the Array is not sorted. We do know that it
    is partially sorted

    :Param array: Array to be searched
    :Param x" Item to be found in the array
    "Return: The index of X in the array, None if it is not in the array
    """

    n = len(array)
    # split the array
    left = array[:n//2]
    right = array[n//2:]

    def isSorted(array):
        """
        Helper function that checks if the array is sorted by comparing the 
        first and last elements of the array

        :Parram array: array to be checked
        :Return: A boolean. True if index 0 is less than index n
        """
        if len(array) == 0:
            return False
        return array[0] <= array[-1]

    index = None
    # if the left is sorted and x is in left
    if isSorted(left) and x >= left[0] and x <= left[-1]:
        index = bSearch(left, x)

    # if the right is sorted and x is in right
    if isSorted(right) and x >= right[0] and x <= right[-1]:
        index = bSearch(right, x)
        if index != None:
            index += len(left)

    # if we found an index return it
    if index != None:
        return index
    else:
        # check through left unsorted
        index = shuffleSearch(left, x)
        if index != None:
            return index
        else:
            # check through right unsorted
            return len(left) + shuffleSearch(right, x)


# testing

array = [13, 18, 25, 2, 8, 10]
item = 8

print(shuffleSearch(array, item))
