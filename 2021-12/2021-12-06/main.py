# Shaun Leung
# Dec 6, 2021

# alright this one is pretty straight forward enough just need to recurse down
# sub trees. They even told you what function you will need to that will help.

# Just gonna do a quick and dirty implimentation

# Nodes will enter unlocked by default
class Node:
    def __init__(self, value=None, right=None, left=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.locked = False

# have to start with a value


class biTree:
    def __init__(self, value) -> None:
        self.root = Node(value)

# add left and right will try to add a value to the right or left of the given
# node. If that space is already occupied it will try to add it to that node
# if no node is specified it will use the root

    def addRight(self, value, node=None):
        if not node:
            node = self.root
        if not node.right:
            node.right = Node(value)
        else:
            self.addRight(value, node.right)

    def addLeft(self, value, node=None):
        if not node:
            node = self.root
        if not node.left:
            node.left = Node(value)
        else:
            self.addLeft(value, node.left)

    # nice and easy function here
    def is_locked(self, node):
        return node.locked

    # this is the function that will do the heavy lifting
    # dont have to worry about checking self only the children
    def dec_locked(self, node):
        # leaf
        if not node.right and not node.left:
            return self.is_locked(node)
        # only left
        if not node.right and node.left:
            return self.dec_locked(node.left) == self.is_locked(node)
        # only right
        if node.right and not node.left:
            return self.dec_locked(node.right) == self.is_locked(node)
        # both
        else:
            return (self.dec_locked(node.right) == self.dec_locked(node.left))

    def lock(self, node):
        # leaf
        if not node.right and not node.left:
            node.locked = True
            return True
        # left
        if not node.right and node.left:
            if self.dec_locked(node.left):
                node.locked = True
                return True
        # right
        if node.right and not node.left:
            if self.dec_locked(node.right):
                node.locked = True
                return True
        # both
        if self.dec_locked(node):
            node.locked = True
            return True
        else:
            return False

    def unlock(self, node):
        # leaf
        if not node.right and not node.left:
            node.locked = False
            return True
        # left
        if not node.right and node.left:
            if self.dec_locked(node.left):
                node.locked = False
                return True
        # right
        if node.right and not node.left:
            if self.dec_locked(node.right):
                node.locked = False
                return True

        # both
        if self.dec_locked(node):
            node.locked = False
            return True
        else:
            return False


# Testing
#                0
#             /     \
#            1      2
#           / \    / \
#          3  4   5   6
# Building the tree
tree = biTree(0)
root = tree.root
tree.addLeft(1)
tree.addLeft(3)
tree.addRight(2)
tree.addRight(6)
tree.addRight(4, root.left)
tree.addLeft(5, root.right)

print("Root lock is " + str(tree.is_locked(root)))

if tree.is_locked(root):
    print("Error: root is locked")

print("Locking the root")
if tree.lock(root) == False:
    print("Error: Root didn't lock")

print("Root lock is " + str(tree.is_locked(root)))

if tree.is_locked(root) == False:
    print("Error: root is unlocked")

print("unlocking the root")
if tree.unlock(root) == False:
    print("Error: Root didn't unlock")

print("Root lock is " + str(tree.is_locked(root)))

# Checking locking in grandchild case
print("Locking grandChild Value 3")

if tree.lock(root.left.left) == False:
    print("Error: Grandchild with value 3 didnt lock")

print("Trying to lock Root")
if tree.lock(root) == True:
    print("Root Locked when it shouldnt have")

print("Root lock is " + str(tree.is_locked(root)))


print("*****************************")
# tree 2 is just a LL
# 0-1-2
tree2 = biTree(0)
tree2.addRight(1)
tree2.addRight(2)
root = tree2.root
# trying to lock root
print("Root lock is " + str(tree2.is_locked(root)))
if tree2.is_locked(root):
    print("Error: root is locked")

print("Locking the root")
if tree2.lock(root) == False:
    print("Error: Root didn't lock")

print("Root lock is " + str(tree2.is_locked(root)))

# This one was a tricky one with passing up the lock status since if its a line
# and the end is false it will pass up a false all the way which would be
# wrong since the tree would be valid for a lock
