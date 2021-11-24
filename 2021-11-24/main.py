# Shaun Leung
# Nov 24, 2021

# alright this problem is very similar to the one from Nov 19, 2021. In fact it
# might be a bit easier since we dont need to worry about edge cases of digits
# and the alphabet containgin 26 letters

# as is the case with most dynamic programing questions start small and work 
# your way up. 

# We know that as more steps are added the number of combinations cannot 
# decrease

# since there are no space or time requirements here we can be a little 
# extravagent and add some variables for clarity. Will still get this done on
# O(N) though

# lets deal with the main question first before moving on to the juicy additions
# at the bottom of the page. Since we can climb 1 or 2 steps we will need to 
# look at the last 2 steps taken and how those two increas the combinations of
# the step that we are currently looking at. 

def stairCombo(n):
    comboTracker = []
    steps = 2
    for i in range(0,n):
        curSum = []

        # technically can hard code this for 2 steps but I want to get a jump
        # on the bonus section
        for j in range(0,steps):
            # we cant take more steps than there are steps that exist
            if j > i:
                break

            # handle when need to look to the left of the 0 index
            if i - (steps- j) < 0:
                curSum.append(1)
            else:
                # add up the previous k steps to get current
                curSum.append(comboTracker[i-(steps-j)])
            
        # update the combinations for the curent step
        comboTracker.append(sum(curSum)) 

    # return the tail which is the total # of combos of n steps
    return comboTracker[-1]


# base question testing
for i in range(1,6):
    print("n = "+str(i))
    print(stairCombo(i))

# Slight change to add the addition of more steps
# ahhh mis understood the question here I though it was steps from 0<=k
# Keeping this here for postarity but deleting the tests
def moreStairCombo(n,k):
    comboTracker = []
    steps = k
    for i in range(0,n):
        curSum = []

        # technically can hard code this for 2 steps but I want to get a jump
        # on the bonus section
        for j in range(0,steps):
            # we cant take more steps than there are steps that exist
            if j > i:
                break

            # handle when need to look to the left of the 0 index
            if i - (steps- j) < 0:
                curSum.append(1)
            else:
                # add up the previous k steps to get current
                curSum.append(comboTracker[i-(steps-j)])
            
        # update the combinations for the curent step
        comboTracker.append(sum(curSum)) 

    # return the tail which is the total # of combos of n steps
    return comboTracker[-1]


# alright going off the syntax of the question k is going to change to an array
# of + ints

# gonna make a few assumptions here too. I am going to return partial combos 
# since n might not be evenly divisable by any of k I will return how many 
# combinations you can get before you run out of stairs.
# now technically this is O(NK) time but I think that is pretty good

# this run through of the functuion helped me clean it up a bit more too. steps
# is a much better name than j. Probably could have saved some time doing this 
# from the starts and then hard coding in [1,2] but c'est la vie
import math
def evenMoreStairCombo(n,k):
    comboTracker = []
    for i in range(0,n):
        curSum = []
        for step in k:
            if (i - step) == -1:
                curSum.append(1)
            if step > i:
                continue
            else:
                curSum.append(comboTracker[i-step])
            
        comboTracker.append(sum(curSum)) 
    
    return comboTracker[-1]

# extended question testing
print("Extended Testing")
steps = [1,2]
print(steps)
for n in range(1,6):
    print("n = "+str(n))
    print(evenMoreStairCombo(n,steps))

steps = [1,3,5]
print(steps)
for n in range(1,7):
    print("n = "+str(n))
    print(evenMoreStairCombo(n,steps))