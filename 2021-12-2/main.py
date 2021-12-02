# Shaun Leung
# Dec 2, 2021

# The contraints on this one are killing me
# brute force would just be O(NM) since we could check every element in A
# against every element in B

# The space restraint hurts too because we could just look for the first double
# and we would have the node.

# if the two lists converge at some point then we now that at the very least the
# last node in both lists will be the same. That means any extra nodes that we
# can ignore would be located at the begining of the lists. This means that if
# the lists are diferrent sizes we can ignore the difference of the length of
# the longer list against the length of the smaller list.


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


def listString(node):
    # lets make things look nice
    string = str(node.value)
    cur = node.next
    while cur:
        string += "->" + str(cur.value)
        cur = cur.next
    return string


def getLen(node):
    # a little helper function
    len = 0
    cur = node
    while cur:
        len += 1
        cur = cur.next
    return len


def findIntersect(nodeA, nodeB):
    # first count the lengths of the nodes
    lenA = getLen(nodeA)
    lenB = getLen(nodeB)

    curB = nodeB
    curA = nodeA
    # traverse the difference
    if lenA > lenB:
        for _ in range(lenA-lenB):
            curA = curA.next
    else:
        for _ in range(lenB-lenA):
            curB = curB.next

    # doesnt matter which one since they have the same length now
    while curA:
        if curA == curB:
            return curA
        curA = curA.next
        curB = curB.next
    return "Error"


# Building tests first
# Challenge test
AB = Node(8, Node(10))
A = Node(3, Node(7, AB))
B = Node(99, Node(1, AB))
print("A = " + listString(A))
print("B = " + listString(B))

print("AB = " + listString(findIntersect(A, B)))
# check if it is the same object
print(AB == findIntersect(A, B))
