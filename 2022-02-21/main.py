# Shaun Leung
# Feb 21, 2022

"""
So this one seems pretty mathy to me and math isnt my strong suite

I suppose I can just brute force this one.
"""

from pydoc import ispackage


def goldbach(num):
    """
    Find 2 prime numbers that sum to the input number

    @num{int}            The number to sum to, bust be even adn greater than 2
    @Return(int,int)     A tuple containing two numbers that sum to num
    """
    if num < 3 or num %2 != 0:
        print("Input invalid")
        return None

    def isPrime(num):
        """
        Checks if a number is prime, only divisible evenly by 1 and itself

        @num{int}           Int to be checked
        @Return{boolean}    True if prime, False otherwise
        """
        for div in range(2,num//2):
            if num % div == 0:
                return False
        return True

    for first in range(2, num):
        second = num - first
        if isPrime(first) and isPrime(second):
            return first, second

for x in range(4,30,2):
    print(x,":",goldbach(x))



"""
Huh interestingly the example does not have the lexicographically smallest answer for 4, wait I am wrong apparently 1 is not prime!
"""