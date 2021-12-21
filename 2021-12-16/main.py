# Shaun Leung
# Dec 21, 2021 Little late since I am moving right now


# First thing that needs to be check is where the front and the end of the
# Took me a little while to figure out what the other palindromes would be fore
# Race but once I figure it out the prohlem actually became much simpler

# started this on JS but after thinkging about it and dipping my toes in I am
# going to change to python for the list sliceing


# We are going to do comparasins from the front and back and always take the
# lexicographically earlier char and insert it into the proper place on the
# side (this is why I want list slicing)
def makePal(string):
    end = len(string)-1
    beg = 0
    while beg < end:
        print(string)
        # same
        if string[beg] == string[end]:
            beg += 1
            end -= 1
            continue
        # front
        elif string[beg] < string[end]:
            string = string[:end+1] + string[beg] + string[end+1:]
            beg += 1
        # end
        else:
            string = string[:beg] + string[end] + string[beg:]
            beg += 1

    return string


string = "azb"

print(string)
print("******")
print(makePal(string))
