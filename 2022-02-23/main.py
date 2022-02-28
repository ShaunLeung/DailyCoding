#Shaun Leung
#Feb 23, 2022

"""
This one screams dynamic programming to me but through a cute mask of 
of chars instead of ints. 

There are quite a few constraints on this one with including every char
as well as returning the smallest substring. First idea was to go char by
char checking constraints but it doesnt remember optimal solutions very
well. 

my next idea is to grab the a list of the two chars we need to hit and 
find the min distance between the two lists. 


Well ignore everything I said before I read this question completely wrong.
New plan is to go through the list and look for the lonest sub-string that 
fits those constraints. then we will recurse until there is no sub string. 
Then we will return that sub-string. 
"""
import copy

def exists(string, chars):
    copyChars = copy.deepcopy(chars)
    for char in string:
        if char in chars:
            copyChars = copyChars.replace(char,'')

    if len(copyChars) ==0:
        return True
    else:
        return False


def subString(string,chars,flag = False):
    """
    Goes through the string from front to back looking for a char in the 
    list of chars. Once one is found it is removed from the copied list of
    chars and records that pos and check from the back and the remaining 
    chars, the pos is then recorded and then it checks betweeen those two
    pos for the rest of the chars. If it finds them all it recurses with 
    the substring.

    If it fails it returns the string it was given.

    @Param{String}      String to check for given characters
    @Param{String}
    """

    if len(string) < len(chars):
        return string

    
    start = None
    end = None
    # Find the first char
    copyChars = copy.deepcopy(chars)
    
    # Check begining
    for i, char in enumerate(string):
        if char in copyChars:
            copyChars = copyChars.replace(char,'')
            start = i
            break

    # check for end
    for i, char in enumerate(reversed(string)):
        if char in copyChars:
            copyChars = copyChars.replace(char,'')
            end = len(string) - i -1
            break
    
    # Check the rest
    if start and end and len(copyChars) > 0:
        for char in string[start+1:end]:
            if char in copyChars:
                copyChars = copyChars.replace(char,'')

    front = None
    subStrings = []
    if len(copyChars) == 0:
       # need to process returns
        sub1 = subString(string[start+1:end],chars,True)    # Both
        sub2 = subString(string[start+1:end+1],chars,True)  # Start
        sub3 = subString(string[start:end],chars,True)      # End
        sub4 = subString(string[start:end+1],chars,True)
        # need to process returns, dont want fails
        if sub1 != string and len(sub1) >= len(chars) and exists(sub1,chars):
            subStrings.append(sub1)
        if sub2 != string and len(sub2) >= len(chars) and exists(sub2,chars):
            subStrings.append(sub2)
        if sub3 != string and len(sub3) >= len(chars) and exists(sub3,chars):
            subStrings.append(sub3)
        if sub4 != string and len(sub4) >= len(chars) and exists(sub4,chars):
            subStrings.append(sub4)

        # grab the least
        front = min(subStrings, key=len)

    # I need to to do the above twice.....but start with the back

    start = None
    end = None
    # Find the first char
    copyChars = copy.deepcopy(chars)
    # check for end
    for i, char in enumerate(reversed(string)):
        if char in copyChars:
            copyChars = copyChars.replace(char,'')
            end = len(string) - i -1
            break

    # Check begining
    for i, char in enumerate(string):
        if char in copyChars:
            copyChars = copyChars.replace(char,'')
            start = i
            break

    # Check the rest
    if start and end and len(copyChars) > 0:
        for char in string[start+1:end]:
            if char in copyChars:
                copyChars = copyChars.replace(char,'')
    
    back = None
    subStrings = []
    if len(copyChars) == 0:
        # need to process returns
        sub1 = subString(string[start+1:end],chars,True)    # Both
        sub2 = subString(string[start+1:end+1],chars,True)  # Start
        sub3 = subString(string[start:end],chars,True)      # End
        sub4 = subString(string[start:end+1],chars,True)
        # need to process returns, dont want fails
        if sub1 != string and len(sub1) >= len(chars) and exists(sub1,chars):
            subStrings.append(sub1)
        if sub2 != string and len(sub2) >= len(chars) and exists(sub2,chars):
            subStrings.append(sub2)
        if sub3 != string and len(sub3) >= len(chars) and exists(sub3,chars):
            subStrings.append(sub3)
        if sub4 != string and len(sub4) >= len(chars) and exists(sub4,chars):
            subStrings.append(sub4)

        # grab the least
        back = min(subStrings, key=len) 
   
    # Return chain
    if not back and not front:
        return string

    if back == None and front:
        return front

    if front == None and back:
        return back

    

    if back and front and len(back) < len(front):
        return back

    if back and front and len(front) <= len(back):
        return front

    if flag == False:
        return None

    return string


# Testing
string = "figehaeci"
set = 'aei'
print("String:", string)
print("set:",set)
print("Substring:",subString(string,set))


"""
Okay This one took me way longer than I thought it would. I hate quite a few
errors in my logic and had to work them out as I was coding. 
"""