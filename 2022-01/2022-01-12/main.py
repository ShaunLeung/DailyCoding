# Shaun Leung
# Jan 12, 2022

"""
This one threw me for a bit of a loop since I was trying to think of ways to do 
this with a constant amount of multiplication operations or some other math 
wizardy. I think what it really comes down to is they want it in less than 
O(n) time where x^n.

Easy solution is that we know x^n+n = x^n * x^n which means that we can just 
divid and conquer saving time when n is even since we only need to do it once. 
Memoization!

Things to look out for are the base cases when n = 1 or 0 with x^0 = 1 and 
n^1 = n.
"""


def pow(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x

    # if exponent is even
    if y % 2 == 0:
        left = pow(x, y//2)
        right = left
    else:
        left = pow(x, y//2)
        right = pow(x, (y//2)+1)

    return left * right


# testing
for i in range(10):
    print("2 ^", i, "=", pow(2, i))
