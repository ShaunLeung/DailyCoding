# Shaun Leung
# Nov 21, 2021

# Ah, the greedy Neighbour I have actually seen this question before and it is 
# dynamic programing question

# As you go through the list of numbers the lighest possible sum cannot 
# decrease it can only stay the same or increase. you will need to look at 
# the las 2 highest possible sums in order to determine if you will take the
# number you are currently looking at.
# 
# Ex. take the greater of array[i] + (sum[i-2]) or sum[i-1] 
#
# This can be done very easily in O(N) time and linear space, though you can
# "cut the fat" and do it in constant space as we dont care about previous sums

def nonAdjSums(array):
    # use three variables to keep track of sums
    # before I used an array of n to keep trak of hihgest possible sum for 
    # each value then just return the tail of that list to get the answer
    sumPrevPrev = 0
    sumPrev = 0
    sum = 0

    for num in array:
        #shift sums over
        sumPrevPrev, sumPrev = sumPrev, sum

        # take num or not
        if sumPrevPrev + num > sumPrev:
            sum = sumPrevPrev + num
        else:
            sum = sumPrev

    return sum


# Challenge Tests
array = [2,4,6,2,5]
print(array)
print(nonAdjSums(array))
print()

array = [5,1,1,5]
print(array)
print(nonAdjSums(array))
print()