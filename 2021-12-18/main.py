# Shaun Leung
# Dec 22, 2021

# So this one seems pretty simple can still do it recursivly
# but we will need a wrapper function to strip out the min of the
# tuples that the recursive function will retur

# first set up tree stuff and add a print function to make it look nice
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print(self):
        print(str(self.value), end=' ')
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()


def getSecondLg(root):
    # base case for no childern

    if not root.left and not root.right:
        return (float('-inf'), root.value)
    # left case
    if root.left and not root.right:
        sLg, lg = getSecondLg(root.left)
        # node is greater than lg
        if lg < root.value:
            lg, sLg = root.value, lg
        # node is between lg and slg
        elif sLg < root.value:
            sLg = root.value

        return sLg, lg

    # right case
    if not root.left and root.right:
        sLg, lg = getSecondLg(root.right)
        # node is greater than lg
        if lg < root.value:
            lg, sLg = root.value, lg
        # node is between lg and slg
        elif sLg < root.value:
            sLg = root.value

        return sLg, lg

    # both case
    # wrote the comparasons a bit different here to save some space
    rsLg, rLg = getSecondLg(root.right)
    lsLg, lLg = getSecondLg(root.left)
    ints = [rsLg, rLg, lsLg, lLg, root.value]
    lg = max(ints)
    ints.remove(lg)
    sLg = max(ints)
    return sLg, lg


def secondLg(root):
    # small wrapper function to strip out the largerst
    return getSecondLg(root)[0]


    # Testing
root = Node(5, Node(3, Node(1), Node(2)), Node(10, Node(0)))
root.print()
print()
print(secondLg(root))
