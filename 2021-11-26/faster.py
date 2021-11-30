import math
import random


def inCircle(x, y, r):
    # time for some maths. if we take the distance of the point to the center of
    # the cirlce we can determine if the point is in the circle by comparing the
    # distance to the radius. If the distance is <= to the radius it is in the
    # circle
    d = math.sqrt((x*x)+(y*y))
    return d <= r


# ignore the drawing so we can use some big numbers
hit = 0
total = 1000000
radius = 100000
for _ in range(0, total):
    x = random.randint(-radius, radius)
    y = random.randint(-radius, radius)
    if inCircle(x, y, radius):
        hit += 1
print(round(hit/total * 4, 3))

# the trick to this and getting more accurate numbers was increasing the radius!
