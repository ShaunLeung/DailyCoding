# Shaun Leung
# Dec 22, 2021

# This one is labeled as easy so it is kind of a hit
# that I dont really need to go hunting for some cool
# optimizations, instead just gonna brute force this one

import math


def getPowerSet(array):
    ps = []
    size = len(array)
    powSize = int((math.pow(2, size)))
    i = 0
    j = 0

    # Run from counter 000..0 to 111..1
    for i in range(0, powSize):
        set = []
        for j in range(0, size):

            if((i & (1 << j)) > 0):
                set.append(array[j])
        ps.append(set)

    return ps


array = ['a', 'b', 'c', 'd', 'e']
print(array)
print(getPowerSet(array))
