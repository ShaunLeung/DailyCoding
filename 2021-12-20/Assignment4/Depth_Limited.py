import math
from Min_Max import Min_Max_Search
import random

class Depth_Limited_Search(Min_Max_Search):
    """
    Will use the random choice algorithm for this section.
    A new parameter will be added for this seach which is called depth and
    limits how far down the tree a search will travel. if the limit is reached
    it will return a random action from the list of actions
    each state knows about its depth.
    """

    def __init__(self,depth):
        """
        need to know a depth cut-off
        :param depth:
        """
        self.depth = depth

    def minimax_decision(self,problem):
        """

        :param problem:
        :return:
        """
        self.problem = problem
        state = problem.state
        best_action = None

        if self.is_max_turn(state):
            best = math.inf * -1
            for act in problem.actions(state):
                val = self.Min_Val(problem.result(state, act))
                if val > best:
                    best = val
                    best_action = act
        else:
            best = math.inf
            for act in problem.actions(state):
                val = self.Max_Val(problem.result(state, act))
                if val < best:
                    best = val
                    best_action = act

        return (best, best_action)

    def Max_Val(self, state):
        """

        :param state:
        :return:
        """
        problem = self.problem
        if problem.is_terminal(state):
            best = problem.utility(state)
        elif problem.cutoff_test(state,self.depth):
            best = problem.eval(state)
        else:
            best = math.inf * -1
            for act in problem.actions(state):
                new_state = problem.result(state, act)

                val = self.Min_Val(new_state)
                if val > best:
                    best = val
        return best

    def Min_Val(self, state):
        """

        :param state:
        :return:
        """
        problem = self.problem
        if problem.is_terminal(state):
            best = problem.utility(state)
        elif problem.cutoff_test(state,self.depth):
            best = problem.eval(state)
        else:
            best = math.inf
            for act in problem.actions(state):
                new_state = problem.result(state, act)
                val = self.Max_Val(new_state)
                if val < best:
                    best = val
        return best