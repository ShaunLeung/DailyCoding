# Shaun Leung
# Nov 19, 2021

# Will need to consider 2 characters at a time walking through the list
# need to consider 10 and 20 since 0 is not a valid mapping and cant be broken
# down.

# since it is all valid combination will have to be multiplication somewhere
# can walk through the list look at 2 characters at a time that will tell us how
# many new combos to add to our running total.
# ex. 11 can be aa or k 2 new additions

# do a jump if 10 or 20
# will need to watchou out for n being odd and OB checks

# No contraints on this question in terms of time or space
# this feels very dynamic programmy there will come a point where we can be
# confident the numbers we have passed will contirubut to the amount of
# combinations and nothing in future numbers will change that


# !!!! is complextiy being added?
# It cannot diminish but can stay the same
# record as a list will need to begining case
#
# Big break through was how much complexity increases the final result
# array[i] = array[i-1] + array[i-2]


def cyphers(array):
    if array == []:
        return 0
    # we know its not empty so pre-load
    complexity = []
    for i, num in enumerate(array):
        if len(complexity) == 0:
            complexity.append(1)
            continue
        if len(complexity) == 1:
            complexity.append(2)
            continue

        # this means we got a 10 or 20
        if num == 0:
            complexity.append(complexity[-1])
            continue
        # if we can make a 11-19,21-26
        if array[i-1] == 1 or (array[i-1] == 2 and num < 7):
            # array[i] = array[i-1] + array[i-2]
            complexity.append(complexity[-1]+complexity[-2])
        else:
            complexity.append(complexity[-1])

    return complexity[-1]


array = [1, 1, 1, 1, 1, 1]
print(array)
print(cyphers(array))
