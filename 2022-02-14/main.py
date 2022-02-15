#Shaun Leung
# Feb 14, 2022

"""
For some reason this one was listed as easy but there are a ton
of edge cases for it. 

First of all the wording is a little ambiguoius so I don't know if
the start and end nodes are included in the sum. I am going to assume 
that they are because they mentioned a path sum. An easier way to word 
this question might have been to turn it into a path finding problem and use
djikstra's for longest path. 

For my answer I think that I am just going to use a nice recursive algorthim 
that grabs the path with the greatist sum with the current node as the start
and then then check that answer that returns against the answer its children
return. 

So I will need 2 functions:

def pathSum(root): will get the greatest path sum or return None if the path is 
not long enough. 

def maxPathSum(root): This function is also recursive and is used to check if we 
need to exlude the root.
"""
import copy

class Node:
    def __init__(self,value, left =None, right = None) -> None:
        self.value = value
        self.right = right
        self.left = left

    def __str__(self) -> str:
        string = ""
        if self.left:
            string += str(self.left)
        string += str(self.value) +' '
        if self.right:
            string += str(self.right)
        return string

root = Node(4,Node(2,Node(1),Node(3)),Node(6,Node(5),Node(7)))


def pathSum(path):
    """
    will get the greatest path sum or return None if the path is 
    not long enough. 

    @Param{list}    A list of nodes in order from the root.
    @return{int}    The longest path sum
    """

    if not path[-1].left and not path[-1].right:
        if len(path)<3: # path is too short
            return None
        else:
            return sum(map(lambda a:a.value,path)) # return leaf

    if not path[-1].right: #check left
        newPath = copy.deepcopy(path)
        newPath.append(newPath[-1].left)
        return pathSum(newPath)

    if not path[-1].left: # check right
        newPath = copy.deepcopy(path)
        newPath.append(newPath[-1].right)
        return pathSum(newPath)

    #check both
    leftPath = copy.deepcopy(path)
    leftPath.append(leftPath[-1].left)
    rightPath = copy.deepcopy(path)
    rightPath.append(rightPath[-1].right)

    leftSum = pathSum(leftPath)
    rightSum = pathSum(rightPath)

    #return the greater sum
    if not leftSum and not rightSum:
        return None
    elif not rightSum:
        return leftSum
    elif not leftSum:
        return rightSum
    else:
        return max(leftSum, rightSum)
    
if 17 != pathSum([root]):
    print("problem with pathSum")


def maxPathSum(root): 
    """
    This function is also recursive and is used to check if we 
    need to exlude the root.
    """

    sums = [pathSum([root])]
    if root.left:
        sums.append(maxPathSum(root.left))
    if root.right:
        sums.append(maxPathSum(root.right))

    sums = [x for x in sums if x]

    if not sums: # if there are no sums
        return None

    return max(sums)

# testing
print(root)
print(maxPathSum(root))

root2 = Node(4,Node(2,Node(100),Node(3)),Node(6,Node(5),Node(7)))
print(root2)
print(maxPathSum(root2))

root2 = Node(4,Node(-200,Node(100),Node(3)),Node(6,Node(5),Node(7)))
print(root2)
print(maxPathSum(root2))