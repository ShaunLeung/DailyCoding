# Shaun Leung
# Feb 7, 2022

"""
This one is pretty interesting in that it is a bunch of logic rules
and you need to apply rules to it and look for contradictions.

I am thinking of building up a model after first checking if an incoming rule
creates a contradiction.

We really only have to deal with ANDs with diagonal directions and then the
transative property.... that is beyond just straight up contradicions
ie. A N B, B N A.

At first I was thinking of making it as simple as possible with just 2
lists for latitude and longitude but that could cause some problems
since they need to be ordered and since we are being fed rules one at a time
there is some room for uncertanty which could allow for variations on the list.

ie. A N B, C N B tells us nothing about A in relation to C so A,C,B and C,A,B
are both valid lists.

My new idea is to use a dictionary for each point that contains a dictionary of directions and points in that direction.
"""


class Point:
    def __init__(self) -> None:
        self.directions = {}
        self.directions['N'] = []
        self.directions['E'] = []
        self.directions['S'] = []
        self.directions['W'] = []

    def __str__(self) -> str:
        return self.directions.__str__()


class Compass:
    def __init__(self) -> None:
        self.points = {}

    def __str__(self) -> str:
        out = ''
        for key, value in self.points.items():
            out += key+": " + value.__str__() + "\n"
        return out

    def update(self, rule):
        source, direction, dest = rule.split(" ")
        # need to initialize the keys
        if source not in self.points.keys():
            self.points[source] = Point()

        if dest not in self.points.keys():
            self.points[dest] = Point()

        if self.check(rule):
            self.add(rule)
            self.add(self.reverse(rule))
        else:
            print("CONTRADICTION")

    def add(self, rule):
        source, direction, dest = rule.split(" ")
        _, rDirs, _ = self.reverse(rule).split(" ")

        for dir in direction:
            if dest not in self.points[source].directions[dir]:  # avoid dups
                self.points[source].directions[dir].append(dest)

            # dealing with transitive property kinda hate this nested nature
            # but need to account for diagonals it will most loop 2 times
            for rDir in rDirs:
                for point in self.points[source].directions[rDir]:
                    if dest not in self.points[point].directions[dir]:
                        self.points[point].directions[dir].append(dest)

    def reverse(self, rule):
        source, direction, dest = rule.split(" ")
        newDir = ""
        for char in direction:
            if char == 'N':
                newDir += "S"
            if char == 'E':
                newDir += "W"
            if char == 'S':
                newDir += "N"
            if char == 'W':
                newDir += "E"

        return dest+" "+newDir+" "+source

    def check(self, rule):
        reverse = self.reverse(rule)
        source, direction, dest = reverse.split(" ")
        _, rDirs, _ = rule.split(" ")

        for dir in direction:
            if source in self.points[dest].directions[dir]:
                return False

            for rDir in rDirs:  # nested here again
                for point in self.points[source].directions[rDir]:
                    if dest in self.points[point].directions[rDir]:
                        return False
        return True


# testing
model = Compass()
model.update("A NW B")
print(model)
model.update("A N B")
print(model)

print("---------------------------------------")
model2 = Compass()
model2.update("A N B")
print(model2)
model2.update("B NE C")
print(model2)
model2.update("C N A")
print(model2)
