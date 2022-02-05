# Shaun Leung
# Feb 5, 2022

"""
This one is pretty interesting in that is very clearly uses bit operations.
"""


def thisOrThat(x, y, b):
    mask = 0
    for i in range(1, 32):
        mask += b**i

    return (x & mask) | (y & ~mask)


print(bin(thisOrThat(255, 24, 1)))
print(bin(thisOrThat(255, 24, 0)))


"""
Okay I figured out how I wanted to solve this one pretty easily but it sure 
took me a long time to figure out how to construct it. The bit mask thing was
esspecially tricky. 
"""
