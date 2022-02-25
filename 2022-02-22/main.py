# Shaun Leung
# Feb 22, 2022

"""
This one is interesting in that you just need to find an answer
even if multiple answeres exist.

plan is to inchworm through the list looking for a solution.
if the sum is too small add a number to the end if it is too 
big remove a number from the start.
"""

def inchworm(list, k):
    """
    Finds a continueous sublist of list that sumes to k

    @list{[int]}        List of givin ints to use
    @k{int}             Value to sum to 
    @Return{[int]}      Sub list of list that sums to k
    """
    start = 0
    end = 0

    while sum(list[start:end+1])!=k and end < len(list):
        if sum(list[start:end+1]) < k:
            end+=1
        else:
            start+=1

    if end < len(list):
        return list[start:end+1]

    return None

# Testsint
list = [1,2,3,4,5]
print(inchworm(list, 9))


"""
No one big problem with this is that it assumes that all numbers are possitve and takes
advantage of that in that bumping up the start will always make the number smaller. But if
there are negative numbers in the list than this doesnt hold up and you need to consider the
super set of of the list....which we have done before on Dec 19, 2021
"""
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

def findSet(list,k):
    for set in getPowerSet(list):
        if sum(set) == k:
            return set
# Testing
list = [1,2,3,4,5]
print(inchworm(list, 9))