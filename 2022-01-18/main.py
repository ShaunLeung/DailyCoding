# Shaun Leung
# Jan 18, 2022

"""
This is an interesing one.  It wants constant look up which means that
we are probabaly dealing with a hash map here, as well as LRU which screams
linked list to me as well. The big problem is how do we cram the two together 
to meet the time complexity restrictions because updating the linked list means
we would normally have to search for the item in the list which would violate
the time complexity restriction.

The solution is to use a hash map...but instead of storing the key value pairs
we can store the mem location of the node in the linked list which will have 
the value. This way we preserve our constant look up time.

Now I am going to cheat a little bit and use Python's dict data type since it is
a hash map already, and I really dont want to code one of those from scratch but
I will code the bits of the linked list that I need.
"""


from linecache import cache
from xml.dom.minicompat import NodeList


class Node:
    def __init__(self, key, value) -> None:
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


class Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def delete(self, node):
        """
        Delete the node passed in and link up its neighbours
        :Param node: The node to be deleted
        """
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # if we delete the head
        if self.head == node:
            self.head = node.next
        # if we delete the tail
        if self.tail == node:
            self.tail = node.prev
        return

    def push(self, node):
        """
        Add a new node to the front of the link list
        :Param node: The node to be added.
        """
        # update node
        node.next = self.head

        # update prev head
        if self.head:
            self.head.prev = node
        # if there was no head, list was empty update tail
        else:
            self.tail = node

        self.head = node
        return


class LRU_Cache:
    def __init__(self, n):
        self.size = 0
        self.max = n
        self.list = Linked_List()
        self.dict = {}

    def set(self, key, value):
        """
        Stores the key value as a node and then stores the node as both a 
        linked list and a dict. That was I can get O(1) look up with the Dict
        and have a nice queue structure with the list. 

        :Param key: Key to be stored
        :Param value: Value to be stored
        """
        # if key already exits
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            # update list
            self.list.delete(node)
            self.list.push(node)
            return

        #space in cache
        if self.size < self.max:
            node = Node(key, value)
            self.dict[key] = node
            self.list.push(node)
            self.size += 1
        # something needs to go
        else:
            # delete the LRU
            out_node = self.list.tail
            self.list.delete(out_node)
            del self.dict[out_node.key]

            # add new
            node = Node(key, value)
            self.dict[key] = node
            self.list.push(node)

    def get(self, key):
        """
        Pretty simple in that if the key exists we can get it in O(1) with the 
        dict and then update the queue. 

        :Param key: The key of a Key, Value pair
        :Return value: The value of a Key, Value pair
        """
        # return None if we dont have it in the cache
        if key not in self.dict:
            return None

        node = self.dict[key]
        value = node.value
        # update pos of node in list
        self.list.delete(node)
        self.list.push(node)

        return value


# Testing
cache = LRU_Cache(3)
cache.set('a', 1)
print("set('a', 1)")
print("get('a'):", cache.get('a'))

cache.set('b', 2)
print("set('b', 2)")
print("get('b'):", cache.get('b'))

cache.set('c', 3)
print("set('c', 3)")
print("get('c'):", cache.get('c'))

cache.set('d', 4)
print("set('d', 4)")
print("get('d'):", cache.get('d'))

# try and get 'a' should retunr none
print("get('a'):", cache.get('a'))

# update b
cache.set('b', 24)
print("set('b', 24)")
print("get('b'):", cache.get('b'))

# check to see if c is removed
cache.set('e', 5)
print("set('e', 5)")
print("get('e'):", cache.get('e'))

print("get('c'):", cache.get('a'))
