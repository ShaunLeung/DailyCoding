# Shaun Leung
# Feb 3, 2022

"""
This one confused me when I saw it on my phone and I thought they wanted
the tree re-rooted, but it simply looks like they want the tree reflected. 
Souldnt take too long, just a simple recursive algorithm should do the trick. 
"""


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def printTree(root):
    print(root.value, end=' ')
    if root.left:
        printTree(root.left)
    if root.right:
        printTree(root.right)


def reflect(root):
    """
    Don't really even have to worry about cases here since we can just swap
    two Nodes for leaf nodes. No matter what we are going to swap the children
    """
    if root.left:
        reflect(root.left)
    if root.right:
        reflect(root.right)
    root.left, root.right = root.right, root.left

    return


# testing
tree = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f')))
printTree(tree)
print()
reflect(tree)
printTree(tree)
print()
