# Shaun Leung
# Nov 15, 2021

# Given Code
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

# getting a feel for the structure and syntax
print(node.val)
print(node.left.val)

# Challenges have to find a way to preserve structure if a branch is empty
# Could use meta data to record tree structure 
# Ex. 0-3. 
# 0 if end Node
# 1 if left only
# 2 if right only
# 3 if both
# could also use B,L,R,E

# dont want to encode any structure Data to the string as that can get messy and
# might have to be parsed out later
# Also encoding a Special char for empty nodes opens up edge cases when the 
# value of a node is the same as an edge case. 

# recursively traverse through the tree 
def serialize(node, meta = []):
    if node.left == None and node.right == None:
        return [node.val] , [0]

    if node.left != None and node.right == None:
        lVal, lMeta = serialize(node.left, meta)
        return [node.val] + lVal , [1] + lMeta

    if node.left == None and node.right != None:
        rVal, rMeta = serialize(node.right, meta)
        return  [node.val] + rVal , [2] + rMeta

    if node.left != None and node.right != None:
        rVal, rMeta = serialize(node.right, meta)
        lVal, lMeta = serialize(node.left, meta)
        return [node.val] + lVal + rVal ,  [3] + lMeta + rMeta 


node_string , node_meta = serialize(node)

print(node_string)
print(node_meta)


# Build tree back up
def deserialize(serialized, node=None):
    data, metaData = serialized
    val = data.pop(0)
    meta = metaData.pop(0)
    returnNode = None
    # this is an end
    if meta == 0:
        returnNode = Node(val)
    if meta == 1:
        returnNode = Node(val, deserialize((data,metaData)))
    if meta == 2:
        returnNode = Node(val, None, deserialize((data,metaData)))
    if meta == 3:            
        returnNode = Node(val, deserialize((data,metaData)))
        returnNode.right = deserialize((data,metaData))

    return returnNode

new_node_string, new_node_meta = serialize(deserialize(serialize(node)))
print(new_node_string)
print(new_node_meta)

# challenge test
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'