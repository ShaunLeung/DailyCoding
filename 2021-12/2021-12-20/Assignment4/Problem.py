#Shaun Leung swl567 11241403
import State
import copy

class problem:

    def __init__(self, size):
        """
        Problem needs to know how big the board is
        :param size:
        """
        self.size = size
        self.state = State.state()

    def is_terminal(self, state):
        """
        Checks to see if there are any more legal moves left on the board\
        We know that that there cannot be queens on the same col b/c of our actions.
        Since we are moving from left to right we only need to check those queens to the right.

        it is a terminal state if there are no possible moves.
        :param state:
        :return: Boolean
        """

        cur_pos = len(state.variables)  # col we are at
        if cur_pos == self.size:
            return True

        # we can check if if a new move is possible  by building a list of possible moves
        # we will start from the assumption that all moves are possible and eliminate them as
        # each queen is examened.

        # set all possible moves to true
        moves = []
        for i in range(self.size):
            moves.append(True)



        for queen in state.variables:
            pos = state.variables.index(queen)  # col of the queen
            # consider row
            moves[queen] = False

            # consider diagonal
            dif = cur_pos - pos
            # ignore spots below range
            if queen - dif >= 0:
                moves[queen - dif] = False

            # ignore spots above range
            if queen + dif < self.size:
                moves[queen + dif] = False

        terminal = False
        for var in moves:
            terminal = terminal or var

        return not terminal

    def actions(self, state):
        """
        we want the item with the highest utitlity
        :param state:
        :return:
        """

        # An action is an int corresponding to the row which is a valid move
        actions = []

        # we cand check if if a new move is possible  by building a list of possible moves
        # we will start from the assumption that all moves are possible and eliminate them as
        # each queen is examened.

        # set all possible moves to true
        moves = []
        for i in range(self.size):
            moves.append(True)

        cur_pos = len(state.variables)
        for queen in state.variables:
            pos = state.variables.index(queen)  # the col that the queen is in.
            # consider row
            moves[queen] = False
            # consider diagonal
            dif = cur_pos - pos
            # ignore spots below range
            if queen - dif >= 0:
                moves[queen - dif] = False
            # ignore spots above range
            if queen + dif < self.size:
                moves[queen + dif] = False

        # build up the list of actions
        i = 0
        for move in moves:
            if move == True:
                var_pos = moves.index(move)
                actions.append(i)
            i += 1

        return actions

    def result(self, state, action):
        """
        apply an action to a state.
        :param state:
        :param action:
        :return: new state
        """

        # create a new state
        new_state = State.state()

        # copy over the old state
        for var in state.variables:
            new_state.variables.append(var)

        new_state.depth = state.depth + 1
        new_state.alpha = state.alpha
        new_state.beta = state.beta

        # preform the action
        new_state.variables.append(action)

        return new_state

    def cutoff_test(self,state, depth):
        """
        checks to see if the given state is paste the given depth
        returns true if it is and false if not
        :param state:
        :param depth:
        :return:
        """
        if state.depth > depth:
            return True
        else:
            return False


