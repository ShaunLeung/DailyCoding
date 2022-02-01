# Shaun Leung
# Feb 1, 2022

"""
This one actually seems pretty easy, since they just want all possible
combinations it is a simple nested loop and build up a list of combinations.

This thing that makes this really easy is that we know all the keys in the mappuings are single digit so this doesnt turn into a nasty dynamic programing
question.

Mmmm a little trickier than I thought at first so I am going to pivot to a
recursive method.
"""


def decode(t9, string, output=[]):
    newOut = []
    # base case
    if len(string) == 0:
        return output
    # initial case
    if output == []:
        for letter in t9[int(string[0])]:
            newOut.append(letter)
    # recursive case
    else:
        for word in output:
            for letter in t9[int(string[0])]:
                newOut.append(word+letter)

    return decode(t9, string[1:], newOut)


t9 = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

string = "23"

for item in list(t9):
    print(item, ":", t9[item])
print(string)
print(decode(t9, string))


"""
Glad I did this problem cause man was I rusty with recursion this morning. Not 
sure if I got enought coffee in my system. 
"""
