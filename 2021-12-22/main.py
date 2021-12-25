# SHaun Leung
# Dec 25, 2021

"""
Well since this one is a few days old it stumped me completely. At first I 
thought it was a dynamic programing with the O(N) time requirement and the 
O(1) space I figured that it would need to use the array index to save space
like other problems that had similar space requirements. 

After some backburner mulling of the question. I decided to look up the 
solution because I was stumped. Turns out it was the strategy I am the 
weakest, bitwise operations. Well its not that the concepts elude me, its just
that I very really think about such a low level of computer science when
programming. 

Well it has been a few days since I looked up the hint so lets see if I can 
remember the strategy. 
"""


def findSingle(array):

    # these variables will keep track of how many times an item has been found
    foundOnce = 0
    foundTwice = 0

    for item in array:

        # if we have seen it once we can add it to the twice variable
        # we check to see if it was found by using AND
        foundTwice = foundTwice ^ (foundOnce & item)

        # well since we are looking at the number we need to add it to the
        # found once variable at the bery least
        foundOnce = foundOnce ^ item

        # now to remove the items from the variabdles we will need to make a
        # bit mask of the complement

        mask = ~(foundOnce & foundTwice)

        # using the mask to remove the items from the variables
        # Becuase we used the compliment of once & twice it will
        # remove the item if it iexisted in both lists
        foundTwice &= mask
        foundOnce &= mask

    return foundOnce


# tests
array = [1, 1, 1, 2, 2, 2, 6]
print(array)
print(findSingle(array))

# negative numbers
array = [1, 1, 1, 2, 2, 2, -6]
print(array)
print(findSingle(array))


"""
Well apparently I did a good job remembering how this solution worked cause
I got in one go. I did spend a bit of time slowly walking through the hints
so I am glad that some of it sunk in. Hopefully the comments are clear enough
"""
