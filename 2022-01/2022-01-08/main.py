# Shaun Leung
# Jan 8, 2022

"""
This question is actually easier than the one I was thinking of!
The one I had in mind was the dynamic programming problem of 
pretty printing where they just give you a string and it needs to 
be formated so that each line is as even as possible. 

In this question
we are told the max a line is able to be so we just need to make the 
decision of whether to take a word or start a new line. Hardest part is 
going to be to turn the string into an array of words rather than characters.

"""


def toSentence(string):
    """
    Turns a string into an array of words.

    :Param string: String to be turned into a sentence
    :Retrun sentence: An array of words.
    """
    word = ''
    sentence = []
    for letter in string:
        if letter != ' ':
            word += letter
        else:
            sentence.append(word)
            word = ''
    sentence.append(word)
    return sentence


def toLines(sentence, m):
    """
    Function to split a sentence up so that there are only m characters per line
    will trim lagging white space when new line is going to be added. Returns 
    False if there is a word thats len is > than m which means there is no way
    it could fit onto a line. 

    :Param sentence: An array of words to be split up into lines
    :Param m: The max amount of characters a single line can contain
    :Return mLines: An array of each line of the sentence with max len m.
        Returns false if a word cannot be fit onto a line.         
    """
    line = ''
    mLines = []
    for word in sentence:
        if len(line) + len(word) <= m:
            line += word
            # adding a space if there is room
            if len(line) - m != 0:
                line += ' '
        else:
            # record the line and start a new one
            # clean up the trailing space if need be
            if line[-1] == ' ':
                line = line[:-1]
            mLines.append(line)
            line = ''

            if len(line) + len(word) <= m:
                line += word
                # adding a space if there is room
                if len(line) - m != 0:
                    line += ' '
            # word is to long even if it has a line of its own
            else:
                return False

    # final append
    if line[-1] == ' ':
        line = line[:-1]
    mLines.append(line)
    return mLines


def prettyPrinting(string, m):
    """
    Simple function to combine the two other utility functions

    :Param string: A string to be split up into lines of max len m
    :Param m: Max len a single line can be
    "Return: An array of lines with each element being max len m
    """
    return toLines(toSentence(string), m)


# Testing
string = "the quick brown fox jumps over the lazy dog"
print(string)
print(prettyPrinting(string, 10))

# test when word is == m
string = "the quick chartreuse fox jumps over the lazy dog"
print(string)
print(prettyPrinting(string, 10))

# test when word is > m
print(prettyPrinting(string, 9))
