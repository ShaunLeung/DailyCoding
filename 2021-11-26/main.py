# Shaun Leung
# Nov 26, 2021

# Alright, this one seemed a little weird and mathy to me so I had to look up
# exactly what they wanted,
# They want a program that uses a specific method, Monte Carlo, to estimate the
# value of Pi. beyond it being just a purely mathematical exercise it
# essentially wants you to create and run a simulation to achieve the result.

# Good news, is this well help flex those graphicaly muscles which I havent used
# in these challenges before. Gonna make it look nice.

# Going to use turtle, since it the first one that popped up from a google
# search.

import random
import turtle
import math

t = turtle.Turtle(visible=False)
t.speed(0)
radius = 350

# Drawing the circle
t.penup()
t.goto(0, -radius)
t.pendown()
t.circle(radius)

# Drawing the square
t.penup()
t.goto(radius, radius)
t.pendown()
t.goto(radius, -radius)
t.goto(-radius, -radius)
t.goto(-radius, radius)
t.goto(radius, radius)

# Checks to see if in in circle


def inCircle(x, y, r):
    # time for some maths. if we take the distance of the point to the center of
    # the cirlce we can determine if the point is in the circle by comparing the
    # distance to the radius. If the distance is <= to the radius it is in the
    # circle
    d = math.sqrt((x*x)+(y*y))
    return d <= r


# maping random dots
hit = 0
total = 1000
for _ in range(0, total):
    t.penup()
    x = random.randint(-radius, radius)
    y = random.randint(-radius, radius)
    t.goto(x, y)
    t.pendown

    if inCircle(x, y, radius):
        t.color("blue")
        hit += 1
    else:
        t.color("red")

    t.dot(5)

# time for some more maths we know the radius of the circle is pir^2 and the
# radius of the square we drew is 4r^2 = 2r * 2r
# from the diagram drawn we know that the area of the suqare is larger than the
# area of the circle.
# This means that if we pick a point with in the square there is a pi/4 chance
# that the dot will be in the circle/all dots.

# Hit       pi
# -----  =  --
# Total     4

# which can be rewriten h/t * 4 = pi
print(round((hit/total)*4, 3))
turtle.mainloop()
