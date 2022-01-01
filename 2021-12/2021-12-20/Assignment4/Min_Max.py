#Shaun Leung swl567 11241403
import math

class Min_Max_Search(object):
    """
    Min max search, this is essentially depth limited seach with the depth being set
    to greater than the size of the game
    """
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
        else:
            best = math.inf * -1
            for act in problem.actions(state):
                val = self.Min_Val(problem.result(state, act))
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
        else:
            best = math.inf
            for act in problem.actions(state):
                val = self.Max_Val(problem.result(state, act))
                if val < best:
                    best = val
        return best

    def is_max_turn(self,state):
        """
        returns true if is Max's turn false if its not
        only need to make it here since the other searches will inherit these
        :param state:
        :return:
        """
        if len(state.variables) % 2 == 0  or len(state.variables) == 0:
            return True
        else:
            return False


    def is_min_turn(self,state):
        """
        returns true if is Min's turn false if its not
        only need to make it here since the other searches will inherit these
        :param state:
        :return:
        """
        if len(state.variables) % 2 == 0 or len(state.variables) == 0:
            return False
        else:
            return True
