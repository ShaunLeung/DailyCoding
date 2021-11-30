# Shaun Leung
# Nov 18, 2021

import ctypes


class Node:
    def __init__(self, value):
        self.value = value
        self.xor = 0


class XORLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__nodes = []

    def add(self, value):
        node = Node(value)
        if self.head is None:  # If list is empty
            self.head = node
            self.tail = node
        else:
            self.tail.xor = id(node) ^ self.tail.xor
            node.xor = id(self.tail)
            self.tail = node
        self.__nodes.append(node)

    def get(self, index):
        if not self.head or index < 0:
            print("Nothing to return")
            return

        cur = self.head
        prev = 0
        for i in range(index):
            next = cur.xor ^ prev
            if next:
                prev = id(cur)
                cur = self.__type_cast(next)
            else:
                print("OB")
                return

        return cur.value

    # method to return a new instance of type

    def __type_cast(self, id):
        return ctypes.cast(id, ctypes.py_object).value


# testing
xorList = XORLL()
xorList.add(0)
xorList.add(1)
xorList.add(2)
xorList.add(3)

for i in range(-1, 5):
    print(xorList.get(i))

# The first and last should fail
