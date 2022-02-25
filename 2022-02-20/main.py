# Shaun Leung
# Feb 20, 2022

"""
This question seems pretty easy as there are no obsitcales in the way 
so pathing isnt really an issue. The big thing I will focus on here is
to make the code a bit more elegant than a ton of if statements for each
direction of movemnet.
"""

def distance(points):
    """
    Takes a list of points and returns the number of steps required to
    move from the first to the last, vitiing all others inbetween in order

    @points{[(int,int)]}     A list of tuples representing x,y coordinants
    @Return{int}            Number steps needed to visit all points in order
    """
    distance = 0
    start = points[0]

    def move(start,end):
        """
        Helper function that will handle the number of steps betweeen each point

        @Start{(int,int)}   The starting point as a tuple
        @End{(int,int)}     The end point as a tuple
        @Retrun{int}        The number of steps to get from start to end
        """
        steps = 0
        startX, startY = start
        endX, endY = end
        while startX != endX or startY != endY:
            if startX < endX:
                startX+=1
            if startX > endX:
                startX-=1
            if startY < endY:
                startY+=1
            if startY > endY:
                startY-=1
            steps+=1
        return steps

    for point in points:
        print(start,"to",point)
        distance += move(start, point)
        start = point

    return distance


# Testing
points = [(0,0),(1,1),(1,2)]
print(points)
print("Moves",distance(points))


"""
Well hate to say it but De Morgans law tripped me up for a bit in the move function
!(A and B) === !A or !B
"""