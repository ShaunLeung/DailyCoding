#Shaun Leung swl567 11241403
import math
class state:
    """
    Variables contains the row location of each queen
    each pos in the variables list is the col of the queen
    queens will be added to the end of the list to keep this structure

    -contains the alpha and beta values for alpha beta pruning
        -Alpha is initialized to negative infinity
        -Beta is initialized to positive infinity

    -contains a records of the depth that the search is being in
        -depth initialized to 0
    """

    def __init__(self):
        """
        Variables is a list of ints
        depth is initalized to 0
        alpha is init to - infinity
        beta dis init to infinity
        """
        self.variables = []
        self.alpha = math.inf * -1
        self.beta = math.inf
        self.depth = 0