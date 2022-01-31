# Shaun Leung
# Jan 12, 2022

"""
This one seems pretty daunting at first but the simple brute force solution
would be just to generate all the possible sub sections and then just go through
them looking for a pair that satisfies the solution. 

No we can make this large amount of possible sub sections much much smaller 
since we know that Sum(subArray) = Sum(array) / 2. This means as soon as we 
encounter a sub array with a sum that is greater than the Sum(array) /2 we can
toss it out and any subsequent sub arrays it would have made. 

Since we are also only dealing with Ints the Total sum needs to be an even 
number for the solution to exist.

The real problem is finding a subset of the array that is equal to the sum/2
Now that I think about it it is really similar to another question that was 
asked, let me see if I can find it. Yup it was the question from Dec 24, 2021
"""

# Dec 24, 2021 code


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

# wrapper


def sameSum(array):
    totalSum = sum(array)
    # if the sum is odd it can't be evenly split
    if not totalSum % 2 == 0:
        return False

    if memoization(array, totalSum//2):
        return True
    else:
        return False


# Testing
array = [15, 5, 20, 10, 35, 15, 10]
print("Can", array, "be split?", sameSum(array))
array = [15, 5, 20, 10, 35]
print("Can", array, "be split?", sameSum(array))
