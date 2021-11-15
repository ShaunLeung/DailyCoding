import random

k = 17
nums = [10,15,3,7]

def sumChecker(nums, k):
    for i, v in enumerate(nums):
        for j, v2 in enumerate(nums[i+1:]):
            if v + v2 == k:
                return True
    return False

# positve check
print(sumChecker(nums, k))

# negative check
nums = [1,15,3,7]
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
        nums.append(random.randint(1,10))
    return nums

k = random.randint(1,10)
nums = generateRandomList(25)
print('k = ' + str(k))
print ('list = ' + str(nums))
print(sumChecker(nums, k))

