# Shaun Leung
# Jan 18, 2022

"""
I think this one needs some sort of hashing function in order for it to
be close to being un biased. Perhaps a fold in there or something.
"""

from audioop import bias
import random


def biased():
    bias = random.randint(1, 4)
    if bias <= 3:
        return 1
    else:
        return 0


def unbiased():
    total = 0
    for _ in range(10):
        total += biased()
    return total % 2


head = 0
tail = 0

bHead = 0
bTail = 0
for _ in range(10000):
    num = unbiased()
    bNum = biased()
    if num == 0:
        head += 1
    else:
        tail += 1

    if bNum == 0:
        bHead += 1
    else:
        bTail += 1

print("biased")
print("heads", bHead)
print("tails", bTail)

print("unbiased")
print("heads", head)
print("tails", tail)

"""
Looks like I was over thinking it just needed a normal hash with I guess 
ten folds on a 10 digit number
"""
