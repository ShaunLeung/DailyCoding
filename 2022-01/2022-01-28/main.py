# Shaun Leung
# Jan 28, 2022

"""
 Easy one today, at least that is how it was tagged.

 So this looks like a scheduling problem with the data entering unorderd so
 it should probably be ordered before we start doing anything too crazy.

 First throught is that back tracking wont work here b/c there is no failcase.

 The big thing here is we dont want to take an interval with too big off a
 difference or else we limit the other intervals we can take.

 I wonder if you can break this down recursively and do some sort of merge
 sort on it... might be tricky.

 Oh I am an idiot, this is much, much easier than I thought looking at the
 sample input and output all it wants it the intervals that are NOT
 enveoloped by another interval
"""


def overlap(array):
    output = []
    array.sort()
    for interval in array:
        if not output:
            output.append(interval)
            continue

        # since they are intervals just check 2nd
        if interval[1] < output[-1][1]:
            continue

        output.append(interval)

    return output


array = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(overlap(array))


"""
Okay....note to self if the question includes tuples do NOT use cause it will 
cause a lot more headaches than it is worth. 
"""
