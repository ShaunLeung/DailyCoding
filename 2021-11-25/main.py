# Shaun Leung
# Nov 25, 2021

# Seems like this can be solved with dynamic programing
# We can start at the first char and work our way through the string a char at 
# a time until the end.

# The question only wants the length of the longest sub string and not the sub
# string itself so that makes things a little bit easier.

# since it want to consider sub string we know that the part we are looking for
# will be all together...self explanitory but its always nice to write it down

# first idea was to itterate through and when a new unique char is found to just
# drop the oldest char and continue on but that doesnt work for examples like
# abaaac since the latest is a and if it is dropped we break the rules because 
# there are now 3 unique chars when we only want two. 

# Then it hit me to create an array that calculates the longest substring 
# possible for the letter that has a matching index in the string.
# Eg. k=2 abcba == [1,2,2,3,2]

# unfortunatly it isnt as nice as some other dymaic programing questions I have 
# done recently where the running total can only get larger but grabbing the 
# largets int out of the array wont impact speed since we will be at O(NK)
# anyway 

# For a split second I thought we might be able to just subtract one if from the 
# running total but I thought of a counter example of k=2 ababc = [1,2,3,4,2].
# not a huge deal just means we will have to calculate the length going 
# backwards from the latest char. 

def uniqueLen(string,k):
    subTotal = []
    for i,char in enumerate(string):
        subTotal.append(subLength(string[:i+1],k))
    print(subTotal)
    return max(subTotal)


def subLength(string,k):
    unique = []
    length = 0
    i = len(string)
    
    while i > 0 and (len(unique) < k or string[i-1] in unique):
        i -= 1
        if string[i] not in unique and len(unique) < k :
            unique.append(string[i])
        length += 1

#    for char in reversed(string):
#        if len(unique) < k or char in unique:
#            if char not in unique:
#                unique.append(char)
#            length += 1
#        else:
#            break

    return length

# light testing of the subLength function
array = "abaac"
print(array)
print(subLength(array,2))

print(array[:-1])
print(subLength(array[:-1],2))

print()

# testing of lengthUnique
print(array)
print(uniqueLen(array,2))

print(array[:-1])
print(uniqueLen(array[:-1],2))

array = "abcba"
print(array)
print(uniqueLen(array,2))

# I thought I might have been missing something and that I could get it to run
# in linear time so I looked up a solution and their validation check to see if
# a string is valid loops 26 times, once for each letter of the alphabet which
# is why they have linear time. Going off that logic one assumption I can make
# is that k is an int between 1 and 26 which would mean my code also runs in
# linear time. I suppose I could always do some checking on it but I dont think
# that is really what the challenge is checking. 


# ehhhhh to make it a little more "correct" I added some conditionals to the 
# loop in the subLength funtion so that the coonditiona; will fail while its 
# entering the loop and not shortly after it enters. I commented out the old 
# loop instead of deleting it because I think it looks nice
