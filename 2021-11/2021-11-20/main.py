# Shaun Leung
# Nov 20, 2021

# This one seems pretty stright forward mostly just navigating a a binary tree
# and counting the number of unival tree trees which is essentially if both children nodes are the same... ends count as both are None

# First step it to make a tree
class biTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def univalCount(node):
    # if at the end of a branch
    if node.left == node.right:
        return 1

    count = 0
    # check your self
    if node.left and node.right:
        if node.left.value == node.right.value:
            count += 1

    # check your kids
    if node.left:
        count += univalCount(node.left)
    if node.right:
        count += univalCount(node.right)

    return count

# set up the tree from the example


root = biTree(0, biTree(1), biTree(
    0, biTree(1, biTree(1), biTree(1)), biTree(0)))
print(univalCount(root))
