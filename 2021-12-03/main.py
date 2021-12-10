# Shaun Leung
# Dec 3, 2021

# So when I first read this I thought it was asking how many lectures could
# maximize in a single classroom. Instead of minimize the numbers of rooms you
# will need for the schedule.

# Not sure if this is the right way to go about questions like this but for some
# reason my mind always wanders towards edge cases and what info is needed to
# avoid them. In this instance it would be if there was a short class say 1
# minute long that could be fit into between two already existing classes.

# I have a feeling this can be done in linear time which would mean that doing
# a pre-sort of the schedule would be out of the question.

# I do have a suspicion that it cant be done in linear time since you will need
# to compare the current lecture to all the the previous ones in the worst case
# that all the lecutres overlap and will need a individual room.

# we can get the earlist start and the latest end in O(N) and do something with
# that information.

# We can also start with the assumption that we will need N rooms and then
# reduce from there as we join lectures together

# another way to look at it, if there is a conflict you will need to add a room.
# You will still need to look at all the previous rooms.

# I think the best way is to just dive into it and get a solution going and work
# from there

def scheduler(array):
    array.sort()
    rooms = []
    minRoom = len(array)
    flag = False
    for start, end in array:
        # pre-load
        if rooms == []:
            rooms.append(end)
            continue

        for room in rooms:
            # can fit a room in
            if start > room:
                room = end
                minRoom -= 1
                flag = True

        if flag:
            flag = False
            continue

        rooms.append(end)
    return minRoom


array = [(30, 75), (0, 50), (60, 150)]
print(scheduler(array))

# not a big fan of the nested loop going to see if I can get rid of theat

# we can just keep track of it like queue if we split the array and then sort
# and then go through both arrays


def scheduler2(array):
    starts, ends = zip(*array)
    starts = list(starts)
    ends = list(ends)
    starts.sort()
    ends.sort()
    rooms = 0
    current = 0
    start = 0
    end = 0
    n = len(array)
    while start < n and end < n:
        # we need a new room
        if starts[start] <= ends[end]:

            # update rooms needed
            current += 1
            rooms = max(current, rooms)

            start += 1
        # a room is free
        else:
            current -= 1

            start += 1
            end += 1

    return rooms


array = [(30, 75), (0, 50), (60, 150)]
print(array)
print(scheduler2(array))

array = [(1, 100), (2, 5), (8, 10), (6, 7)]
print(array)
print(scheduler2(array))

array = [(1, 100), (2, 99), (3, 98), (64, 97)]
print(array)
print(scheduler2(array))

# The sorts are kinda really the least elegant thing here but I like this
# solution of spliting it into 2 lists sorting and then going through keeping
# track of how many rooms are needed.
