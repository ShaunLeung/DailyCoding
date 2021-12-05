# Shaun Leung
# Dec 5, 2021

# This feels very similar to the auto complete question from last month
# (nov 23) so I am going to borrow the tree structure code from that answer.

# Borrowed code ( I will still have to add a few more functions to the
# auto tree class)
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
    def add(self, dic):
        # traverse the tree building nodes when needed.
        for word in dic:
            # start at the root for each new word
            cur = self.root
            for letter in word:
                if letter in cur.next:
                    cur = cur.next[letter]
                else:
                    cur.next[letter] = Node()
                    cur = cur.next[letter]
            cur.value = word

    # recursively go through the tree and grab words
    def getNextWords(self, node, string):
        # base case
        if len(string) == 0:
            return node.value
        if string[0] not in node.next and node.value:
            return node.value
        # look at the sub trees for all next words
        if string[0] in node.next:
            return self.getNextWords(node.next[string[0]], string[1:])
        else:
            return None

    def getSentence(self, string):
        node = self.root
        words = []
        letters = 0
        while letters < len(string):
            word = self.getNextWords(node, string[letters:])
            if not word:
                return None
            letters += len(word)
            words.append(word)
        if letters == len(string):
            return' '.join(words)
        else:
            return None


array = ['quick', 'quant', 'brown', 'the', 'th', 'fox']
string = "thequickbrownfox"
tree = autoTree()
tree.add(array)
print(array)
print(string)
print(tree.getSentence(string))

array = ['bed', 'bath', 'bedbath', 'and', 'beyond']
string = "bedbathandbeyond"
tree = autoTree()
tree.add(array)
print(array)
print(string)
print(tree.getSentence(string))

array = ['quick', 'quant', 'brown', 'the', 'th', 'fox']
string = "bedbathandbeyond"
tree = autoTree()
tree.add(array)
print(array)
print(string)
print(tree.getSentence(string))
