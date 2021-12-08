# Shaun Leung
# Dec 8, 2021

# Alright this one is pretty interesting in that there are quite a few
# restrictions which are actually hints. We know we need to be able to
# create a solution that can only pass through the list once, which means
# that we are not meant to know the length of the list.

# Also constant space means that we can't make a copy of the list and then
# return the copy

# node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeK(node, k):
    if k < 1:
        print("Error: K too low: K must be 1<=k<=n")
        return
    # move k links into the list, this is okay becasue we know k<n
    # this also means we can never remove the first item of the list
    cur = node
    saved = cur
    for _ in range(k+1):
        try:
            cur = cur.next
        except:
            print("Error: K too high: K must be 1<=k<=n")
            return

    # get to the end of the list
    while cur:
        cur = cur.next
        saved = saved.next

    # do the delete
    # Saved will at furthest be n-1 at k=0
    saved.next = saved.next.next


head = Node(0)
cur = head
for i in range(1, 100):
    cur.next = Node(i)
    cur = cur.next

cur = head
while cur:
    print(cur.value, end=" ")
    cur = cur.next

removeK(head, 1)
print("*************************")

cur = head
while cur:
    print(cur.value, end=" ")
    cur = cur.next
