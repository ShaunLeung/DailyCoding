# Shaun Leung
# Jan 29, 2022

"""
This one seems pretty easy at first. My first thoughts were to just
go through each list poping off the head and building up a new list.
Another idea is that this is essentially the last part of a merge
sort, since the sorting of all the seperate arrays has already been done. 

dealing with the k lists is easy, if we can merge 2 we can merge them all. 
"""


class linked:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
        self.tail = None

    def append(self, node):
        cur = self.head
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def print(self):
        cur = self.head
        if not self.head:
            return

        while cur.next:
            print(cur.value, end=" ")
            cur = cur.next
        print(cur.value)


class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


def mergeSort(list1, list2):
    out = linked()
    left = list1.head
    right = list2.head
    n = list1.length
    m = list2.length
    leftCount = rightCount = 0

    # merge
    while leftCount < n and rightCount < m:
        if left.value < right.value:
            out.append(left)
            left = left.next
            leftCount += 1
        else:
            out.append(right)
            right = right.next
            rightCount += 1

    # clean up
    while leftCount < list1.length:
        out.append(left)
        left = left.next
        leftCount += 1

    while rightCount < list2.length:
        out.append(right)
        right = right.next
        rightCount += 1

    return out


def kSort(lists):
    if not lists:
        return lists
    out = lists[0]

    for i in range(1, len(lists)):
        out = mergeSort(out, lists[i])

    return out


# building up the lists
lists = [linked() for _ in range(5)]
i = 1
for _ in range(10):
    for list in lists:
        list.append(Node(i))
        i += 1

for list in lists:
    list.print()


kSort(lists).print()
