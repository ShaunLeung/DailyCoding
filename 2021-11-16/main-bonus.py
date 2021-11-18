# Shaun Leung
# Nov 16, 2021

# bonus question to get practice with this type of solution

# Things we know:
# elements cannot be negative
# elements will be of max size n-1
# contant space and linear time

# how can we cheat*
# clearly supposed to use array index to store info
# negative # are fair game
# could also use multiple of the array size as a flag

# things to keep in mind
# when looking at elements make sure to use abs
# also check if the element is > n and to subtract in if so
# we can ignore cases where a double has already been found

# Things to do
# flag indexes negative that they exist in the array
# add n to to index to indicate that a double has been found

def findDup(array):
    n = len(array)
    for num in array:
        # normalize for -OB and -
        if num < -n:
            temp = abs(num + n)
        else: 
            temp = abs(num)

        # dont care about found dups
        if array[temp] < -n:
            continue
        
        # we know num is between -n and n
        # Check if we have seen it before
        # if so flag it as a dup by putting it OB
        if array[temp] < 0:
            array[temp] -= n
        else:
            # if this is the first time we have seen it (any + #) negate it
            array[temp] = -array[temp]

    # output array is allowed in constant space since we need to return an array
    # between size 0 and n
    outArray = []
    # grab all indexes with values <= -n
    for i, num in enumerate(array):
        if num <= -n:
            outArray.append(i)
    return outArray

# Testing
# Challenge tests

array = [1,2,3,6,3,6,1]
print(array)
print(findDup(array))
print()

array = [1,2,3,4,2]
print(array)
print(findDup(array))
print()

#random test
import random
n = 7
array = []
for i in range(0,n):
    num = random.randint(0,n-1)
    array.append(num)

print(array)
print(findDup(array))
print()

# things to keep in mind
# -Make sure to normalize to a temp First!!!!!!!!!!