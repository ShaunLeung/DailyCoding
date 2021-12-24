#Shaun Leung swl567 11241403

class PvP(object):
    def __init__(self, p1, p2, problem):
        """
        :param p1: search strategy for player one
        :param p2: search strategy for player two
        :param problem: the problem.
        """
        self.player_one = p1
        self.player_two = p2
        self.problem = problem

    def play(self):
        """
        Lets the 2 players play the game
        runs until a terminal state is found
        :return:
        """
        while not self.problem.is_terminal(self.problem.state):
            result = self.player_one.minimax_decision(self.problem) # player one's move
            self.add_move(result)

            if self.problem.is_terminal(self.problem.state):
                break

            result = self.player_one.minimax_decision(self.problem)  # player two's move
            self.add_move(result)

        # game is over
        if self.problem.utility(self.problem.state) < 0:
            return -1
        else:
            return 1

    def add_move(self,result):
        """
        adds the move to the problem
        :param result:
        :return:
        """
        self.problem.state.variables.append(result[1])  # add the move to the problem
        self.problem.state.depth += 1
