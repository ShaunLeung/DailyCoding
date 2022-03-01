# Shaun Leung
# Feb 24, 2022

"""
This one is pretty straight forward but requires a bit of setup
"""

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.right = None
        self.left = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def add(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            self.tail = node
            node.left = temp
            temp.right = node
        self.count += 1
    
    def isPalindrome(self):
        if self.count ==0:
            return True

        start = self.head
        end = self.tail
        while start.left != end and start != end:
            if start.value != end.value:
                return False

            start = start.right
            end = end.left

        return True

    def print(self):
        node = self.head
        while node:
            print(node.value,end=' ')
            node = node.right
        print()
# testing
list1 = LinkedList()
list1.add(1)
list1.add(2)
list1.add(1)
list1.add(1)
list1.print()
print(list1.isPalindrome())

list1 = LinkedList()
list1.add(1)
list1.add(2)
list1.add(2)
list1.add(1)
list1.print()
print(list1.isPalindrome())
            