# Shaun Leung
# Jan 1, 2021

"""
Love tree questions. This one isnt that bad once you realize that
you can be a little loose with the tree balancing. In that since there
is no structure infered in the list (balanced tree vs. list).
"""
"""
Node set up for the trees
"""




import math
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
Prints out the tree in pre-order can be used to check the answer
"""


def printTree(root):
    if not root:
        return ''
    out = root.value
    out += printTree(root.left)
    out += printTree(root.right)
    return out


"""
This is going to be a recursive function that will return the 
"""


def preOrder(array, parent=None):
    if not array:
        return None
    parent = Node(array.pop(0))

    n = len(array)
    leftTree = array[:math.floor(n/2)]
    rightTree = array[math.floor(n/2):]

    parent.left = preOrder(leftTree, parent)

    parent.right = preOrder(rightTree, parent)
    return parent


array = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
print(array)

preRoot = preOrder(array)
print(printTree(preRoot))


"""
Very similar solution but the tree just needts to be borken at a different point
at the middle rather than the start
"""


def inOrder(array, parent=None):
    if not array:
        return None

    n = len(array)
    h = math.floor(n/2)
    parent = Node(array[h])

    leftTree = array[:h]
    rightTree = array[h+1:]

    parent.left = preOrder(leftTree, parent)

    parent.right = preOrder(rightTree, parent)
    return parent


array = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
print(array)

inRoot = inOrder(array)
print(printTree(inRoot))
