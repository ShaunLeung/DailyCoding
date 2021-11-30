# Shaun Leung
# Nov 16, 2021

# FAILED

# Hints from clue
#   -Linear time
#   -Constant space, no delaring n variables or set of n size


# will need to carefully control what info is needed and can be discarded
# we can ignore neagtive #s and 0 as they are not regarded as positive.
# duplicates should not make a difference if we are keeping running totals
# dont consider number that are greater than the array size

import random


def missingNo(array):
    # set up our totals
    i = 1
    l = float('inf')
    h = float('-inf')
    for num in array:
        # dealing with neagtive and 0
        if num <= 0 or num > len(array):
            continue

        # dealing with updating possible answer
        if num == i:
            i += 1
            if i == l:
                i += 1
                if i == h:
                    i += 1

        # dealing with lowest possible that has been seen
        if num < l and num >= i:
            l = num

        # dealling with highest seen  and possible
        if num > h and num >= i:
            h = num

    return i


# Testing
# Challenge examples
array = [3, 4, -1, 1]
print(array)
print(missingNo(array))
print()

array = [1, 2, 0]
print(array)
print(missingNo(array))
print()

# My example
array = [1, 4, 3, 2]
print(array)
print(missingNo(array))
print()


# Falls this case as the function forgets about 4 and never records 3
array = [4, 7, 2, 3, 1]
print(array)
print(missingNo(array))
print()

# empty
array = []
print(array)
print(missingNo(array))
print()

# random
array = []
for i in range(0, 5):
    n = random.randint(-5, 5)
    array.append(n)

print(array)
print(missingNo(array))
print()


# Clue use the indexes of the array to store info.
# shift everything <=0 and returns the index of the first + #
def shiftOmit(array):
    cur = 0
    for i, num in enumerate(array):
        if num <= 0:
            array[cur], array[i] = array[i], array[cur]
            cur += 1
    return cur


def findPositive(array):
    # Flip negative
    for num in array:
        if abs(num) <= len(array):
            if array[abs(num)-1] > 0:
                array[abs(num)-1] *= -1

    # find first positive index
    first = 1
    for num in array:
        if num <= 0:
            first += 1
        else:
            return first
    return first


def missingPos(array):
    return findPositive(array[shiftOmit(array):])


print("New Algo")
# Challenge examples
array = [3, 4, -1, 1]
print(array)
print(missingPos(array))
print()

array = [1, 2, 0]
print(array)
print(missingPos(array))
print()

# My example
array = [1, 4, 3, 2]
print(array)
print(missingPos(array))
print()


# Falls this case as the function forgets about 4 and never records 3
array = [4, 7, 2, 3, 1]
print(array)
print(missingPos(array))
print()

# empty
array = []
print(array)
print(missingPos(array))
print()

# random
array = []
for i in range(0, 5):
    n = random.randint(-5, 5)
    array.append(n)

print(array)
print(missingPos(array))
print()
