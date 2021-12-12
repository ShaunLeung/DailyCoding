# Shaun Leung
# Dec 12, 2021s
#
# The screams dynamic programing to me esspecially if they want this done in
# linear time. The constant space kind of throws me but lots of dynamic
# programing questions can be reduced to contstant space.
#
# I was thinking of having an array and calculating the water at each element
# but that would require O(N) space.  Will at the very leas need to keep a
# running total.
#

# intrinish things about this problem we can glean
# the first and last element cannot hold any water or else it would run off
# this means the main loop only need to check between 1 and N-1

# keep track of left and rights max hights

# need to slowly prgress through the list and fill to the 2nd highest


def rain(array):
    total = 0
    left = 0
    right = 0
    rightIndex = len(array)-1
    leftIndex = 0

    while(leftIndex <= rightIndex):

        # if left is the min
        if array[leftIndex] < array[rightIndex]:
            # update the left max
            if left < array[leftIndex]:
                left = array[leftIndex]
            # add to the total
            else:
                # no need for abs b/c we checked that in the if
                total += left - array[leftIndex]

            # move on
            leftIndex += 1

        # if right is the min do the same but for the right
        else:
            if right < array[rightIndex]:
                right = array[rightIndex]
            else:
                total += right - array[rightIndex]
            rightIndex -= 1

    # return the answer
    return total


# testing
array = [2, 1, 2]
print(array)
print(rain(array))
print()

array = [3, 0, 1, 3, 0, 5]
print(array)
print(rain(array))
print()
