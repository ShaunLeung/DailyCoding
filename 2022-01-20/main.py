# Shaun Leung
# Jan 20, 2022

"""
So the easy way of doing this is to just generate all the possible combination
and return the max now it can be stored in a 3d array or a single array but the
time complextiy is... not great. Looking at O(N^3), but lets code it up anyway
"""


import time


def badProduct(array):
    possible = []
    n = len(array)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:  # cant use the same # twice
                    possible.append(array[i]*array[j]*array[k])

    return max(possible)


array = [-10, -10, 5, 2]
print(array)
print(badProduct(array))


"""
Now I think this can be sped up a bit since we only really need to look at the extreme here, lets say the top and bottom three numbers so 6 in total
"""


def betterProduct(array):
    # alright this is a bit of cheating but our function is made for big arrays
    # so anything smaller than 6 can just be done by the bad function I'll do
    # some timings later to prove its faster.
    if len(array) < 6:
        return badProduct(array)

    extreme = [float('-inf'), float('-inf'), float('-inf'),
               float('inf'), float('inf'), float('inf')]
    for num in array:
        # biggest #s
        if num > extreme[0]:
            extreme[0], extreme[1], extreme[2] = num, extreme[0], extreme[1]
            continue
        elif num > extreme[1]:
            extreme[1], extreme[2] = num, extreme[1]
            continue
        elif num > extreme[2]:
            extreme[2] = num
            continue

        # smallest #s
        if num < extreme[-1]:
            extreme[-1], extreme[-2], extreme[-3] = num, extreme[-1], extreme[-2]
            continue
        elif num > extreme[-2]:
            extreme[-2], extreme[-3] = num, extreme[-2]
            continue
        elif num > extreme[-3]:
            extreme[-3] = num
            continue
    # also a little bit of cheating but we know the size of the array is 6
    return badProduct(extreme)


# so to test this I am just going to copy and paste the elements of the previous
# array a couple of times which should keep the max product the same
array = [-10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10,
         -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5,
         2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -
         10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10,
         -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5,
         2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -
         10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10,
         -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5,
         2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -
         10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10,
         -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5, 2, -10, -10, 5,
         2, -10, -10, 5, 2]
print(array)
start = time.time()
print("Bad", badProduct(array))
print(time.time()-start)

start = time.time()
print("Better", badProduct(array))
print(time.time()-start)
