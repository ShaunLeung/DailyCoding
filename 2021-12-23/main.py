# Shaun Leung
# Dec 26, 2021

"""
Looking at the problem I was thinking it was similar to the the classroom
booking question from last month but after looking at it again I am thinking
that it is more similar to the N queens problem a couple days ago in that I
will need to implement some back tracking since we need to use every entry in
the itinerary list.

Since the right itinerary is the one that is lexicographically minimal we can 
do some sorting and I am not going to worry too much about the time complexity right now. 

First step in solving this is going to be converting the itinerary list to 
dictionary where the key will be the departing airport and the values will be a 
lexicographically sorted list. 

This way we can try the first one and if it doesnt lead to a solution then the next one can be tried.
"""
import copy  # passing by reference can lead to errors. Just make a copy


def makeDic(array):
    dic = dict()
    for flight in array:
        org, dest = flight
        if org in dic.keys():
            dic[org].append(dest)
        else:
            dic[org] = [dest]

        dic[org].sort()

    return dic


def makeList(org, dic, list):

    # if a key exits
    if org in dic.keys():

        # we can iterate since the values are sorted
        for dest in dic[org]:
            # copy for the recusion and possible back tracking
            newList = copy.deepcopy(list)
            newDic = copy.deepcopy(dic)

            # removing the attempted flight from the coppied dic
            newDic[org].remove(dest)
            if newDic[org] == []:
                newDic.pop(org)

            # adding the dest to the list
            newList.append(dest)

            branch = makeList(dest, newDic, newList)

            # failed ending
            if branch == []:
                return []
            else:
                return branch

    # No flights so we either have the correct answer or not
    else:
        if dic:
            return []
        else:
            return list


# wrapper function


def makePlan(array, org):
    dic = makeDic(array)
    list = makeList(org, dic, [org])
    if list:
        return list
    else:
        return None


array = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
org = 'YUL'
print(array)
print(org)
print(makePlan(array, org))
print()

array = [('SFO', 'COM'), ('COM', 'YYZ')]
org = 'COM'
print(array)
print(org)
print(makePlan(array, org))
print()

array = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
org = 'A'
print(array)
print(org)
print(makePlan(array, org))
