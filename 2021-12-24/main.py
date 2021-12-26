# Shaun Leung
# Dec 26, 2021

"""
I was thinking the answer to this challenge would be a dynamic programming
but with so many combinations it is a little too tough.

Since there is no time and space restriction it can always be brute forced.
Thankfully we have code from the 19th on making power sets. Also we can return
any subset as a valid answer. 
"""

import time
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


def bruteForce(array, k):
    ps = getPowerSet(array)

    for set in ps:
        if k == sum(set):
            return set
    return None


# test
array = [12, 1, 61, 5, 9, 2, 1, 61, 5, 9, 2, 1, 611, 61, 5, 9, 2, 1, 61, 5, 9]
k = 24
print(array)
print(k)
start = time.time()
print(bruteForce(array, k))
end = time.time()
print(end-start)
print()

"""
Now for the above solution we did a ton of work and then did a ton more work to
dig the correct answer out of the pile of possibilities. 

We can probably make this a bit more efficient by stopping when an answer is 
found. we can also ignore a few cases where the sume of a set is < than K since
we dont need to deal with negaticve numbers. We can also ignore the case where 2
sets sum to the same number since we only really need an answer and we dont 
care which one it is. 

going to make a dictionary where the keys are sums and the values are the items 
that sum up to the key.
"""


def memoization(array, k):
    dic = dict()
    dic[0] = []

    for item in array:
        keys = dic.keys()
        for key in list(keys):
            newKey = item + key

            # found k so we can leave
            if newKey == k:
                return dic[key] + [item]

            # the sum is new and valid
            if newKey not in keys and newKey < k:
                dic[newKey] = dic[key] + [item]

    # couldnt find a subset
    return None


# testing
print(array)
print(k)
start = time.time()
print(memoization(array, k))
end = time.time()
print(end-start)
