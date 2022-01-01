# Shaun Leung
# Jan 1, 2022

"""
Another tree problem! I actually think I did this exact problem when I first 
started at the U of S. It was in C so it was a bit of a little lower level 
than Python.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
Pretty simple recursive problem is that you keep on passing up the answer if
the value of the node is a operator and if it is a number we know it is a leaf
and that number can just be passed up
"""


def evaluate(node):
    if node.value == '+':
        return evaluate(node.left) + evaluate(node.right)
    if node.value == '-':
        return evaluate(node.left) - evaluate(node.right)
    if node.value == '*':
        return evaluate(node.left) * evaluate(node.right)
    if node.value == '/':
        right = evaluate(node.right)
        # small check do make sure we are not diving by 0
        if right == 0:
            right = 1
        return evaluate(node.left) / right

    # if it isnt an operator then it  must be a number and we can regard
    # it as a lead and just return the value.
    return node.value


"""
Prints out the tree in pre-order
"""


def printTree(root):
    if not root:
        return ''
    out = str(root.value)
    out += printTree(root.left)
    out += printTree(root.right)
    return out


root = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
print(printTree(root))
print('Answer', evaluate(root))
