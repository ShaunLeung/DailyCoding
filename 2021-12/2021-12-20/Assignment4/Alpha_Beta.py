import math
from Min_Max import Min_Max_Search

class Alpha_Beta_Search(Min_Max_Search):
    """
    Prunes edges that result in fruitless searches
    2 new variables were added to the state class which are
    Alpha and Beta which keep track of the best min and max
    of that branch of the tree.

    Inherits Min_Max search cause it has some handy functions like is_max_turn and is_min_turn
    """

    def minimax_decision(self,problem):
        """
        Should have same out
        :param problem:
        :return: the utility of the expected final game and the move to make
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
        Looks for a utility value from its children
        or if it is ad terminal state returns a utility value
        :param state:
        :return:
        """
        problem = self.problem
        if problem.is_terminal(state):
            best = problem.utility(state)

        else:
            best = math.inf * -1
            for act in problem.actions(state):
                val = self.Min_Val(problem.result(state, act))
                if val >= state.beta:
                    return math.inf
                if val > best:
                    best = val
                    if best > state.alpha:
                        state.alpha = best

        return best

    def Min_Val(self, state):
        """
        Looks for a utility value from its children
        or if it is ad terminal state returns a utility value
        :param state:
        :return:
        """
        problem = self.problem
        if problem.is_terminal(state):
            best = problem.utility(state)

        else:
            best = math.inf
            for act in problem.actions(state):
                val = self.Max_Val(problem.result(state, act))
                if val <= state.alpha:
                    return math.inf *-1
                if val < best:
                    best = val
                    if best < state.beta:
                        state.beta = best
        return best
