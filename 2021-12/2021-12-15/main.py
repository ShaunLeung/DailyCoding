# Shaun Leung
# Dec 15, 2021

# This one is pretty fun and simple. I think the way I am going to tacke this
# is to build up a head that way I can maintain order in the list to easily get
# the mean.

import heapq
import math


def runningMed(array):
    medians = []

    for i, num in enumerate(array):
        medians.append(num)
        medians.sort()
        if i % 2 == 0:
            print((medians[int((i/2))-1] + medians[int(i/2)])/2)
        else:
            print(medians[math.floor(i/2)])
    print(medians)


array = [2, 1, 5, 7, 2, 0, 5]
runningMed(array)


# heap sort didnt work like I wanted to I just added then sorted for each #element added.
