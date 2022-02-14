# Shaun Leung
# Feb 14, 2022

"""
Doing this one in Python since it uses dictionary's a bit more natrually than JS.

So this question is interesting in that you either print out all the course ID or 
none of them since it says " Return a sorted ordering of courses such that we can dinish all
courses." That means the easy way is to just check that there is a valid dictionary of courses 
such that all courses can be taken and then just return a sorted list of the dictionary keys. 
"""

import copy

def allValid(classes):
    taken = []
    courses = copy.deepcopy(classes)

    while len(list(courses)) > 0:
        prev = len(taken) # keep track of how many courses we can take
        # add courses 
        for course in list(courses):
            
            if len(courses[course]) == 0:
                taken.append(course)
                del courses[course]
            else:
                prereqsNeeded = len(courses[course])
                prereqsTaken = 0
                for prereq in courses[course]:
                    if prereq in taken:
                        prereqsTaken+=1
                if prereqsTaken == prereqsNeeded:
                    taken.append(course)
                    del courses[course]

        # no courses were added and there are still courses to take
        # we can exit
        if len(taken) == prev:
            return False

    return True

def sortCourses(classes):
    if allValid(classes):
        keys = list(classes.keys())
        keys.sort()
        return keys
    else:
        return None


# testing
courses = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
print(sortCourses(courses))


"""
sorting the keys didnt feel great and I am sure there is a better whay to do things
"""

def courseSort2(classes):
    taken = []
    courses = copy.deepcopy(classes)

    while len(list(courses)) > 0:
        prev = len(taken) # keep track of how many courses we can take
        # add courses 
        for course in list(courses):
            
            if len(courses[course]) == 0:
                taken.append(course)
                del courses[course]
            else:
                prereqsNeeded = len(courses[course])
                prereqsTaken = 0
                for prereq in courses[course]:
                    if prereq in taken:
                        prereqsTaken+=1
                if prereqsTaken == prereqsNeeded:
                    taken.append(course)
                    del courses[course]

        # no courses were added and there are still courses to take
        # we can exit
        if len(taken) == prev:
            return None
    taken.sort()
    return taken

# testing
courses = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
print(courseSort2(courses))

"""
Okay that wasent too hard to clean up a bit. 
"""