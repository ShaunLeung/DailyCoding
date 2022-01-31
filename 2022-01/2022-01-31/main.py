# Shaun Leung
# Jan 31, 2022

"""
Pretty simple in that we just need to recurse down the tree and pass up the deepest node, if there is a tie, just take the latest one or something
"""


from re import L


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def findDeepest(node, depth=0):
    # leaf
    if not node.left and not node.right:
        # the deepest node will have no children
        # set up with depth first to help the max function on both
        deepest = (depth+1, node)

    # go right
    elif not node.left:
        deepest = findDeepest(node.right, depth+1)

    # go left
    elif not node.right:
        deepest = findDeepest(node.left, depth+1)

    # consider both
    else:
        deepest = max(findDeepest(node.left, depth+1),
                      findDeepest(node.right, depth+1))

    # if we are the start of the recursion we only want the node
    if depth == 0:
        return deepest[1]
    else:
        return deepest


# Testing
tree = Node('a', Node('b', Node('d')), Node('c'))
print(findDeepest(tree).value)
