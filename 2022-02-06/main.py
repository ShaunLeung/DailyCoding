# Shaun Leung
# Feb 6, 2022

"""
This one is very similar to the classic "valid brackets" question. Interestingly
enough this one seems a little easier since there is only one flavour of bracket

The other thing that needs to be  kept in mind is that you cant return early 
from this one if a violation is encounteredm since you need to count them.

Rules:
Need to start with an opening and end with a closing, anything else
should be removed

Closed bracket must close an open one. 
"""


def brackets(string):
    """
    Open keeps track of how many nested brackets there are and once one is 
    closed it is decremented. 

    remove keeps track of how  many closing brackets are without an opening 
    pair. 

    By returning the sum of the two at the end we get the number of brackets 
    that need to be removed.
    """
    remove = 0
    open = 0
    for bracket in string:
        if bracket == '(':
            open += 1
        elif bracket == ')':
            if open == 0:
                remove += 1
            else:
                open -= 1

    return remove + open


# Testing
string = "()())()"
print(string, "has", brackets(string), "brackets to be removed")

string = ")("
print(string, "has", brackets(string), "brackets to be removed")
