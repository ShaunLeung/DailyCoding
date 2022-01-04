# Shaun Leung
# Jan 4, 2022

"""
Thought about this one for a while but the constant time restriction had me
stumped. Turns out it is a linked hash map, something I rember learning about in
class but have completely forgot about because it really isnt something I use
every day. It might be a good idea to go through my old notes and start
re-learning the time and space complexities for some common data strcutures. I will try and find some notes/texts from that class and link it in todays entry.

essentiall the data is stored as nodes and arranges in a hash map for the quick
access and then also as a linked list so that the least recently used item can
removed from the list.

Things that need to be done.
-Set up Nodes
    -deleting
    -adding to the head
-Set up Cache
    -keep track of max capacity
    -keep track of current count
        -note there is no way to remove and item w/o replacement
    -head and tail of list
    -hash map of Nodes
        -adding
        -deleting


This problem is kinda just a lot of tedious programing
"""


"""
Pretty simple node structure. Keeps track of values and keys
as well as its neighbours
"""


class Node:
    def __init__(self, key, value) -> None:
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class Cache:
    """
    the Cache need to be initialized with a size so that we know when an item
    needs to be replaced in the cache. 
    """

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.count = 0
        self.map = {}
        self.head = None
        self.tail = None

    """
    Very simple function that just just hooks up a node's neighbours to 
    eachother removing the node from the list
    Param: Node
    Return: None
    """

    def deleteNode(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # tail check, need to update if we are deleting it
        if node == self.tail:
            self.tail = node.prev

    """
    since we only care about new nodes being added we can just have one 
    function to puch new nodes to the head of the list.
    Param: Node
    Return: None
    """

    def push(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node

        # tail check need to initialize
        if not self.tail:
            self.tail = node

    """
    The function that does the most heavy lifting in the cache class since it 
    needs to both create and delete new nodes from both the list as well as the 
    map, as well as keep track of the count (though it can only be incremented)
    Param: Key, Value
    Return: None
    """

    def set(self, key, value):
        # updating and item in the cache
        if key in self.map:
            node = self.map[key]  # get the node
            node.value = value  # update the value
            # doesn't actually delete the node just makes the list forget about
            # it but we still have the memory addess to add it to the front
            self.deleteNode(node)
            self.push(node)

        else:
            node = Node(key, value)

            if self.count < self.capacity:  # we can still add more
                self.count += 1

            else:
                # kinda awk but I dont want to make a new function for unshift
                # make room
                if self.tail:
                    tempTail = self.tail.prev
                else:
                    tempTail = None

                # this is the reason we need to save the key in the node
                del self.map[self.tail.key]
                self.deleteNode(self.tail)
                self.tail = tempTail

            # add the node to the list and map
            self.map[key] = node
            self.push(node)

    """
    Pretty simple will look through the map to see if the key exists
    if it does it returns the value, if it doesn't it will return None
    it also needs to push the node to the front since it was used
    Param: Key
    Return: Value, None on Fail
    """

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            # pushing node to the front
            self.deleteNode(node)
            self.push(node)
            return node.value
        else:
            return None


# Testing
size = 2
cache = Cache(size)
print("Cache created with size of ", size)
print("Get('a') ", cache.get('a'))
cache.set('a', 1)
print("Set('a', 1)")
print("Get('a') ", cache.get('a'))

cache.set('b', 2)
print("Set('b', 2)")
print("Get('b') ", cache.get('b'))

cache.set('c', 3)
print("Set('c',3)")
print("Get('c') ", cache.get('c'))

# try and get a
print("Get('a') ", cache.get('a'))

# update b
print("Get('b') ", cache.get('b'))

# add d
cache.set('d', 4)
print("Set('d',4)")
print("Get('d') ", cache.get('d'))

# try and get c
print("Get('c') ", cache.get('c'))


"""
Closing Thoughts
This one was actually a fun one to code and not as "tedious" as I thought it 
was going to be. Once I understood what was going on it actually became pretty 
simple through to be fair the dict data type was doing a lot of the heavly 
lifting here and if I had to code that from scatch it would be excuciating. 

"""
