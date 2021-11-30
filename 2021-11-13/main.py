import random

k = 17
nums = [10, 15, 3, 7]

# by using a set the time complexity of a lookup is reduced to O(1), on avg,
# which means the total time complextiy of the sum checker can be reduced to
# O(n)


def sumChecker(nums, k):
    setCheck = set()
    for i, v in enumerate(nums):
        if (k-v) in setCheck:
            return True
        else:
            setCheck.add(v)
    return False


# positve check
print(sumChecker(nums, k))

# negative check
nums = [1, 15, 3, 7]
print(sumChecker(nums, k))

# empty list check
k = 0
nums = []
print(sumChecker(nums, k))

# empty list check
k = 17
nums = []
print(sumChecker(nums, k))

# random check

# Generate a random list of numbers


def generateRandomList(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(1, 10))
    return nums


k = random.randint(1, 10)
nums = generateRandomList(25)
print('k = ' + str(k))
print('list = ' + str(nums))
print(sumChecker(nums, k))
