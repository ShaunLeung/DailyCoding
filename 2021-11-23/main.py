# Shaun Leung
# Nov 23, 2021

# Alright, so the brut force way would to be just check s against eacch item in 
# the possible strings. Having to do this each time is not the best. We can 
# cheat a bit and chop off lots of possible paths so that the return time is 
# quicker. 

# eg.        root
#          /  |  \
#         a  ..   z
#       / | \
#      a ..  z

# by return serialized sub trees we can cut down on time. The downside is we 
# gotta put in the time to tree-ify the set of possible strings...but we only 
# have to do it once. 

class Node:
    def __init__(self):
        # The value is a word exits
        self.value = None
        # the keys for this dictionary are letters a->z and the keys are nodes
        self.next = {}

class autoTree:
    def __init__(self):
        self.root = Node()
    
    # adds nodes to the tree as needed and store the words
    def add(self,s):
        cur = self.root

        # traverse the tree building nodes when needed. 
        for letter in s:
            if letter in cur.next:
                cur = cur.next[letter]
            else:
                cur.next[letter] = Node()
                cur = cur.next[letter]

        cur.value = s

    # serializes the sub tree
    def getSubTree(self,node):
        words = []
        #add self if exits
        if node.value:
            words.append(node.value)

        # recurse down the tree
        for key,link in node.next.items():
            if link:
                words += (self.getSubTree(link))
        # return hits
        return words 

    # returns the start node of a sub tree
    def findSub(self, s):
        cur = self.root
        for letter in s:
            cur = cur.next[letter]
        return cur

    # returns a list of possible words
    def autoComplete(self, s):
        return self.getSubTree(self.findSub(s))

root = autoTree()
array =  ["dog", "deer", "deal"]
for word in array:
    root.add(word)

print(root.autoComplete("de"))

# I am sure there is already a library made for doing this sort of thing but it
# was good practice making a data structure

# Going to try and make it a bit leaner, not a huge fan of setting up each 
# letter in the node.next to be None by default
