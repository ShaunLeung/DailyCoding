# Shaun Leung
# Jan 02, 2022

"""
I am not sure if I am mis interpretting this question but can you not just go 
through the list element by element and swap it with another random element in 
the list. Now this will mean that the elements earlier on are swapped more often
than ones later on. 
"""
import random
import math


def rand(k):
    return random.randint(1, k)


def shuffle(deck):
    for i, _ in enumerate(deck):
        r = rand(52)-1
        deck[i], deck[r] = deck[r], deck[i]
    return deck


deck = list(range(1, 53))
print(deck)
print(shuffle(deck))
