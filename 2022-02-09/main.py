# Shaun Leung
# Feb 9, 2022

"""
Again not sure why this one is labled as med, maybe I am just getting better 
as a coder. 

Plan is to recurse through the tree checking the main node and then checking 
the children. Only slight hickup is to check for None type when at leafs or
single paths. 
"""

class Node:
    def __init__(self,value, left=None,right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


    def print(self):
        if self.left:
            self.left.print()
        
        print(self.value,end=' ')

        if self.right:
            self.right.print()
        

def balanceCheck(root):
    if root.left:
        if root.left.value <= root.value:
            left = balanceCheck(root.left) # recurse
        else:
            left = False # fail case
    # single path or leaf
    else:
        left= True
    if root.right:

        if root.right.value >= root.value:
            right = balanceCheck(root.right) # recurse
        else:
            right = False # fail case
    # single path or leaf
    else:
        right = True
    
    return left and right


# Testing
root1 = Node(4,Node(2,Node(1),Node(3)),Node(6,Node(5),Node(7)))
root1.print()
print()
print(balanceCheck(root1))
root2 = Node(4,Node(6,Node(7),Node(5)),Node(2,Node(3),Node(1)))
root2.print()
print()
print(balanceCheck(root2))
        
