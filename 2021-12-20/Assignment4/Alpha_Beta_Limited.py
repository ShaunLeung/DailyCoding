import math
from Depth_Limited import Depth_Limited_Search
import random

class Alpha_Beta_Limited_Search(Depth_Limited_Search):
    """
    This search combines both depth limited and alpha beta pruning
    following the trend of inheriting usefull things
    """

    def __init__(self,depth):
        """
        We need to know the depth cutoff
        :param depth:
        """
        self.depth = depth

    def minimax_decision(self,problem):
        """

        :param problem:
        :return:
        """
        self.problem = problem
        problem = self.problem
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
        does Alpha Beta Pruning and Depth Limited
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
                if val >= state.beta:
                    return math.inf
                if val > best:
                    best = val
                    if best > state.alpha:
                        state.alpha = best
        return best

    def Min_Val(self, state):
        """
        does Alpha Beta Pruning and Depth Limited
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
                if val <= state.alpha:
                    return math.inf *-1
                if val < best:
                    best = val
                    if best < state.beta:
                        state.beta = best
        return best