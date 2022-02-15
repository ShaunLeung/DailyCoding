# Shaun Leung
# Feb 13, 2022

"""
Love me some tree questions. This one is interesting in how I am going to set it up.
Since the Given tree there might be any number of children. 
Normally how I make trees in Python I have right and left labled as the next nodes, 
since there needs to be any number of children I am thinking of using a list of nodes
with the nodes going left to right with increasing indices. 

First thing to do is write code to find sub trees that are valid BST (binary search tree) 
which I had to look up. 

The next thing is to write a simple function to measure the depth of a tree so that we 
can decided which tree to take when there are multiple BST to choose from. 


Also I am going to steal a bit of code from Feb 9, don't worry I am going to be making some 
modifications.
"""

class Node:
    def __init__(self,value, nodes=[]) -> None:
        self.value = value
        self.nodes = nodes


    def print(self):
        n = len(self.nodes)

        for node in self.nodes[:n//2]:
            node.print()
        
        print(self.value,end=' ')

        for node in self.nodes[n//2:]:
            node.print()
        

def balanceCheck(root):
    """
    This will check to see if the given node is valid BST. Note that the nodes
    may have any number of children but a valid BST will have at most 2.

    Note that if there is only one child it does not matter if it is greater or
    less than the root's value since it could represent left or right. It still 
    needs to be checked though. 

    @Param{Node}        The root of the tree to be looked at.
    @Return{Boolean}    True if valid BST, False otherwise. 
    """
    # Leaf
    if len(root.nodes)  == 0:
        return True
    # one path
    if len(root.nodes)  == 1:
        return balanceCheck(root.nodes[0])
    # two paths
    if len(root.nodes)  == 2:
        # fulfills the requirements for a BST
        if root.nodes[0].value <= root.value and root.nodes[1].value >= root.value:
            return balanceCheck(root.nodes[0]) and balanceCheck(root.nodes[1])
        else:
            return False
    # more than 2
    else: 
        return False

# tests
root1 = Node(1,[])
if not balanceCheck(root1):
    print("Leaf check failed")
    root1.print()

root2 = Node(1,[Node(2)])
if not balanceCheck(root2):
    print("One path check failed")
    root2.print()

root3 = Node(2,[Node(1),Node(3)])
if not balanceCheck(root3):
    print("Valid BST check failed")
    root3.print()

root4 = Node(2,[Node(3),Node(1)])
if balanceCheck(root4):
    print("InValid BST check failed")
    root4.print()

root5 = Node(2,[Node(3),Node(1), Node(4)])
if balanceCheck(root4):
    print(">2 check failed")
    root4.print()

def depthCheck(root):
    """
    Function to return the max depth of a tree.

    @Param{Node}        The root of the tree to be looked at.
    @Return{int}        The max depth of the tree. 
    """
    if root == None:
        return 0

    # Leaf
    if len(root.nodes)  == 0:
        return 1
    childDepths = []

    # if there are children
    for node in root.nodes:
        childDepths.append(depthCheck(node))

    # return greatest depth + 1 for itself
    return max(childDepths) + 1

if depthCheck(root2) != 2:
    print("Error with depthCheck")


def largestBST(root):
    """
    Takes in a tree with no max on children and retruns the largest BST

    @Param{Node}    The root of the tree to be examend. 
    @Return{Node}   The root of the largest BST in the given tree.
    """

    # Check Self and base case
    if balanceCheck(root):
        return root
    
    size = 0
    largest = None
    # Check Children
    for node in root.nodes:
        bst = largestBST(node)
        if depthCheck(bst) > size:
            size = depthCheck(bst)
            largest = bst
    
    return largest

node = largestBST(root3)
node.print()
