# Shaun Leung
# Dec 22, 2021

# So still behind on the coding challenges which kind of gives me an unfair
# adv. of being able to think about the challenge over a bit longer of a time

# This one seems like it is pretty straight forward. It did trip me up at the
# beginning becuase I thought they wanted the answer in one pass but the
# question says linear time so that makes thing easier since there are 3
# types of characters that means we need 2 passes since the second pass will
# take care of the remainging character'

def colourSort(string):
    i = 0
    red = 0

    # red pass
    while i < len(string):
        if string[i] == 'r':
            # This is the swap
            string[red], string[i] = string[i], string[red]
            red += 1

        i += 1

    # Green pass
    # Since all reds are in the front we cand now loop through
    # a slice string[red:]
    i = red+1
    green = i
    while i < len(string):
        if string[i] == 'b':
            # This is the swap
            string[green], string[i] = string[i], string[green]
            green += 1

        i += 1
    return string


# Testing (I am lazy and just going to consider lower case but you could always
# pass it through a to upper or something)
string = ['g', 'b', 'r', 'r', 'b', 'r', 'g']
print(string)
print(colourSort(string))
