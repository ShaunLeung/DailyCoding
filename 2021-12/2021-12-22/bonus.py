# Shaun Leung
# Dec 25, 2021

"""
This problem really reminded me of another problem that I saw
about 2-3 years ago when I was reading an article about 
programing questions during interviews. So I am going to try and
solve it. The main thing that I remember from the probelm is that
it had to something to do with bitwise operations and that it 
completely stumped me when I saw it. 

The Question
Givin two unsigned int X and Y, swap them and return them 
so that X=Y and Y=X. You cannot create any variables to do this. 
"""


def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y


# testing
x = 4
y = 1
print((x, y))
print(swap(x, y))

x = -4
y = 1
print((x, y))
print(swap(x, y))

"""
Since I was in the headspace of doing bit operations I suppose it made
things a bit easier. Still kidna proud that I was able to work it out, 
since I remember the article saying that this problem was kind of unfair
to ask in a interview. 

Had to look up a bit of how python handles signed ints and maybe I got the 
wording of the question wrong because the function seems to handle negative ints fine. 
"""
