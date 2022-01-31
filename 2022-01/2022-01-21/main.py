# Shaun Leung
# Jan 21, 2022

"""
This one seems pretty easy in that the problem is straight forward and it will
follow a pattern. I think the tricky part will be making it elegant in storing
the number and incrementing the individual digits.
"""


def getDigitSum(num):
    return sum(list(map(int, str(num))))


def findPerfect(n):
    """
    Ehhh instead of doing things mathy and looking for patterns and checking
    for edge cases lets just infinite look and look for perfet #'s.

    Folowing a pattern can get a little dicey at large numbers 
    """
    num = 18    # 19 is the first perfect # and it makes the loop a little
    # cleaner
    count = 0
    while(True):
        if getDigitSum(num) % 10 == 0:
            count += 1
            if count == n:
                return num
        num += 1


# Testing
n = 123
print(str(n)+"th perfect number is:", findPerfect(n))
