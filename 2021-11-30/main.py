# Shaun Leung
# Nov 29, 2021

# I think I might have the wrong idea with this one. my mind went to brute force
# which would be just to check each sub array of size k but that means that the
# time would be O(NK) and not O(N)

# hints they give is that is also needs to be done in constant space and you can
# alter the array which means there might be some index funkery but since the
# elements are not restrained that messes this up. also the numbers are ints so
# negatives are a posibility

# Ahhhhh the above is wrong. thats what reading will get you. you get to use k
# space

# the time complexity restraint is the one that gets me though since Max() would
# take at least 0(K)

# Going to look this one up b/c im stumped
# looks like there are 3 different solutions that fit the time constraint.
# the deque solution is really nice in that you remove useless elements from
# consideration. and you use your k space to hold the indexes of the elements to
# be considered.

# alright time to close the page and see if I can code this from memory. and
# make it more pythonic!

# Deque Maximum Sliding Window

from collections import deque


def maxNSlide(array, k):
    n = len(array)
    qi = deque()

    # Load the first window
    for i in range(k):
        # trim usless elements, first part is a guard against empty array
        while qi and array[i] >= array[qi[-1]]:
            qi.pop()
        # if its needed add it
        qi.append(i)

    # do the rest of the array
    for i in range(k, n):
        # print what we got
        print(array[qi[0]], end=' ')

        # slide the window over
        while qi and qi[0] <= k-i:
            qi.popleft()

        # trim usless again, vut the tail off of qi
        while qi and array[i] >= array[qi[-1]]:
            qi.pop()

        qi.append(i)

    # Print out one last time
    print(array[qi[0]], end=' ')


# Challenge test
array = [10, 5, 2, 7, 8, 7]
k = 3

maxNSlide(array, k)
print()

# GfG test
array = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k = 4
maxNSlide(array, k)


# recap now at first glance there are a few nested loops here but those are
# limited by n in that for every run through of the outer loop that adds an
# element the inner loop will run to remove that element making it 2n times.
