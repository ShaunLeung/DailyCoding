# Shaun Leung
# Jan 24, 2022

"""
This one is nice and easy. Shouldnt take too long to even get the LL framework
setup
"""


class Node:
    def __init__(self, value, next=None) -> None:
        self.next = next
        self.value = value


def reverseLL(head):
    """
    Reverses the linked list where the tail is now the head and the head is the 
    tail
    """
    cur = head
    prev = None

    while cur.next != None:
        # parrallel assignmnet makes this easy
        cur.next, prev, cur = prev, cur, cur.next

    cur.next, prev = prev, cur

    return cur


def printLL(head):
    """
    simple funtion to print out a linked list
    """
    cur = head
    while cur.next != None:
        print(cur.value, end="")
        cur = cur.next
    print(cur.value)


linkedList = Node(1, Node(2, Node(3, Node(4, Node(5)))))
printLL(linkedList)
printLL(reverseLL(linkedList))
