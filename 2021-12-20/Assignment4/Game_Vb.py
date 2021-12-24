#Shaun Leung swl567 11241403
from Problem import problem
import State
import random
class problem_Vb(problem):

    def __init__(self, size):
        """
        needs to know how big of a board we have
        a starting state is also created on init
        :param size:
        """
        self.size = size
        self.state = State.state()

    def utility(self, state):
        """
        Checks to see if we are in a terminal state.
        if we are it checks who won
        if there are an odd number of quees on the board player1 won if there are even then player 2 won
        :param state:
        :return:
        """
        if self.is_terminal(state):
            if len(state.variables) % 2 == 0:
                return -1 * len(state.variables)
            else:
                return 1 * len(state.variables)

    def eval(self,state):
        """
        pick a random possible utility
        :param state:
        :return:
        """
        choice = random.randint(len(state.variables),self.size)
        if choice % 2 == 0:
            return choice * -1
        else:
            return choice