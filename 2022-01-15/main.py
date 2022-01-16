# Shaun Leung
# Jan 16, 2022

"""
There is probabaly a mathematical solution to this problem that would make it
easy and could also help make a dynamic programing answer but I think I want
to solve it the brute force way and just do all the Knights tours on an nxn 
matix.

Wait this is actually backtracking since the knight needs to visit all squares 
at least once so if you get to a point where the knight has no valid moves and 
there are still unvisited squares on the board, you have to backtrack. 

Also I notice that the question doesnt specify where the knight starts. Does 
that mean we need to conisder the knight starting from any of the spots on
the board?

Main function is probabaly going to be recursive. and if I hae to consider
every square as a possible starting location then that can be in a wrapper. 

splitting up pos into rank and file so I can keep track of things easier. 

First step is to initialize the board.
Code Possible moves (there are 8)
Check board state to see if a move is valid
Check if there are unvisited spots on the board
"""
import copy
from webbrowser import get


def isDone(board):
    """
    Checks to see if every square in the board has been visited
    :Param board:       The board to be checked
    :Return Boolean:    True if all square in board are true
    """
    for rank in board:
        for sqr in rank:
            if not sqr:
                return False
    return True


def isValid(rank, file, board):
    if board[rank][file]:
        return False
    return True


def getMoves(rank, file, board):
    """
    Gonna pack each move into a tuple to make things easier tours
    will have to unpack them. Will only pack moves that are on the board


    :Param rank:    The x pos on a board
    :Param file:    The y pos on a board
    :Param board:   The board state
    :Return moves:  A list of moves as a tuple
    """
    n = len(board)  # it's a square so...
    moves = []
    # generating moves
    # left moves
    if file-2 > 0:
        if rank-1 > 0 and isValid(rank-1, file-2, board):
            moves.append((rank-1, file-2))
        if rank+1 < n and isValid(rank+1, file-2, board):
            moves.append((rank+1, file-2))

    # down moves (direction not correctness)
    if rank+2 < n:
        if file-1 > 0 and isValid(rank+2, file-1, board):
            moves.append((rank+2, file-1))
        if file+1 < n and isValid(rank+2, file+1, board):
            moves.append((rank+2, file+1))

    # right moves
    if file+2 < n:
        if rank-1 > 0 and isValid(rank-1, file+2, board):
            moves.append((rank-1, file+2))
        if rank+1 < n and isValid(rank+1, file+2, board):
            moves.append((rank+1, file+2))

    # up moves
    if rank-2 > 0:
        if file-1 > 0 and isValid(rank-2, file-1, board):
            moves.append((rank-2, file-1))
        if file+1 < n and isValid(rank-2, file+1, board):
            moves.append((rank-2, file+1))

    return moves


def tour(rank, file, board):
    """
    Check to see if done. If so return 1

    Next it will call a helper function to generate a list of moves.
    Next it will recursively try those moves and return the sum of those
    moves.

    :Param rank:    The x pos on a board
    :Param file:    The y pos on a board
    :Param board:   The board state
    :Return:        Base cases 1 if Succesful tour, 0 if not
                    Recursive sum of children
    """

    # make the move
    board[rank][file] = True

    # check if done
    if isDone(board):
        print("Tour Done")
        return 1

    tours = 0
    moves = getMoves(rank, file, board)
    for move in moves:
        tours += tour(move[0], move[1], copy.deepcopy(board))
    if tours == 0:
        print("Dead end")
    return tours


def knightsTour(n):
    # initialize board
    board = [[False for _ in range(n)] for _ in range(n)]
    return tour(0, 0, board)


print(knightsTour(8))
