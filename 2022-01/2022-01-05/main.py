# Shaun Leung
# Jan 5, 2022

"""
This is a pretty intense question for programming challenge
I spuuose if this was an interview question you could get away with
some pseudo code.

My strategy to solve this one is going to be back tracking. just gonna
go left to right top to bottom trying different numbers until it leads
to a solution with an answer. if I ever get an invalid answer then it will
back track to the last valid state.

The tricky part of this one is keeping track of the valid state of the board
Rows and Cols are easy enough but the sub boxes could be a little tricky

blank spaces will be regarded as 0 and a number if they are filled.

Doing the propper thing since its so much coding this time arround and writting
function documentation and making unit tests. 
"""
import copy  # going to need this to pass boards back and forth


def printBoard(board):
    """
    Simple function to make the board look better on the terminal

    :Param board: board to be printed
    :Return None:
    """
    for row in board:
        print(row)
    print()


def validRows(board):
    """
    Checks each row of the board to make sure there are no duplicates

    :Param board: The entire sudoku board to be checked
    :return: Boolean that describes if the board is in a valid state
    """
    for row in board:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for cell in row:
            if cell != 0:
                if cell in numbers:
                    numbers.remove(cell)
                else:  # duplicate number
                    return False
    return True


# Rows Test
fail = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]]

correct = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
           [5, 2, 9, 1, 3, 4, 7, 6, 8],
           [4, 8, 7, 6, 2, 9, 5, 3, 1],
           [2, 6, 3, 4, 1, 5, 9, 8, 7],
           [9, 7, 4, 8, 6, 3, 1, 2, 5],
           [8, 5, 1, 7, 9, 2, 6, 4, 3],
           [1, 3, 8, 9, 4, 7, 2, 5, 6],
           [6, 9, 2, 3, 5, 1, 8, 7, 4],
           [7, 4, 5, 2, 8, 6, 3, 1, 9]]

if validRows(fail) == True:
    print("Invalid rows passed ")

if validRows(correct) == False:
    print("Valid rows failed ")


def validCols(board):
    """
    Check each col of the board to make sure the are no duplicates

    :Param board: The entire sudoku board to be checked
    :return: Boolean that describes if the board is in a valid state
    """
    for i in range(len(board)):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(len(board)):
            if board[j][i] != 0:
                if board[j][i] in numbers:
                    numbers.remove(board[j][i])
                else:  # duplicate number
                    return False
    return True


# Cols Test
if validCols(fail) == True:
    print("Invalid cols passed ")

if validCols(correct) == False:
    print("Valid cols failed ")


def validBox(box):
    """
    Check sub box to make sure there are no duplicates

    :Param board: A 3x3 sub box of the board to be checked
    :return: Boolean that describes if the box is in a valid state
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in box:
        for cell in row:
            if cell != 0:
                if cell in numbers:
                    numbers.remove(cell)
                else:  # duplicate number
                    return False
    return True


# test box
boxFail = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]

boxCorrect = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

if validCols(boxFail) == True:
    print("Invalid box passed ")

if validCols(boxCorrect) == False:
    print("Valid box failed ")


def validSubBoxes(board):
    """
    Takes 9 slices of the board and checks each of the 9 sub boxes
    to make sure the are in a valid state. 

    :Param board: The entire sudoku board to be checked
    :return: Boolean that describes if the board is in a valid state
    """

    # want to skip by 3 here
    for i in range(0, 9, 3):
        subRow = board[i:i+3]

        for j in range(0, 9, 3):
            sub = []
            sub.append(subRow[0][j:j+3])
            sub.append(subRow[1][j:j+3])
            sub.append(subRow[2][j:j+3])
            if validBox(sub) == False:
                return False
    return True


# Sub Box Test
if validSubBoxes(fail) == True:
    print("Invalid sub boxes passed ")

if validSubBoxes(correct) == False:
    print("Valid sub boxes failed ")


def validBoard(board):
    """
    This function will check the board's rows, cols and sub boxes to make
    sure it is in a valid state.

    :Param board: The entire sudoku board to be checked
    :return: Boolean that describes if the board is in a valid state
    """
    if validRows(board) == False:
        return False

    if validCols(board) == False:
        return False

    if validSubBoxes(board) == False:
        return False

    return True

# Valid Board Test


if validBoard(fail) == True:
    print("Invalid board passed ")

if validBoard(correct) == False:
    print("Valid board failed ")


def hasBlanks(board):
    """
    Checks the board to see if there are any blanks remaining

    :Param board: The entire sudoku board to be checked
    :return: Boolean that describes if the board has blanks
    """
    for row in board:
        for cell in row:
            if cell == 0:
                return True
    return False


# hasBlanks test
missingNo = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
             [5, 2, 9, 1, 3, 4, 7, 6, 8],
             [4, 8, 7, 6, 2, 9, 5, 3, 1],
             [2, 6, 3, 4, 1, 5, 9, 8, 7],
             [9, 7, 4, 8, 6, 3, 1, 2, 5],
             [8, 5, 1, 7, 9, 2, 6, 4, 3],
             [1, 3, 8, 9, 4, 7, 2, 5, 6],
             [6, 9, 2, 3, 5, 1, 8, 7, 4],
             [7, 4, 5, 2, 8, 6, 3, 1, 0]]

if hasBlanks(correct) == True:
    print("Boad has no blanks but failed")

if hasBlanks(missingNo) == False:
    print("Board has a blank but passed ")


def isSolved(board):
    """
    This one is pretty easy we can check and make sure that there are no 
    0's in the board and that it is in a valid state. If both of these pass
    the board is solved. 

    :Param board: The entire sudoku board to be checked
    :return: Boolean that describes if the board is solved
    """
    if validBoard(board) == False or hasBlanks(board) == True:
        return False

    return True


# isSolved test
if isSolved(fail) == True:
    print("Invalid board passed isSolved ")

if isSolved(correct) == False:
    print("Solved board failed ")

if isSolved(missingNo) == True:
    print("Unsolved board passed ")


def solve(board):
    """
    This function will attempt to recursively solve the puzzle. it will first
    check if the puzzle is valid and if it is will return the solved puzzle. if
    it isnt it will try a number and recurse with the new number added to the
    board.

    :Param board: The sudoku board to be solved
    :return: A sudoku board that is a little more solved or None if the board 
    passed was invalid
    """
    if board == None:
        return None

    # check to see if the board is solved
    if isSolved(board):
        print("Solved!")
        return board

    if validBoard(board) == False:
        return None

    # printBoard(board)
    # find the next blank
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                for num in range(1, 10):
                    newBoard = copy.deepcopy(board)
                    newBoard[i][j] = num
                    newBoard = solve(newBoard)
                    if newBoard != None:
                        return newBoard

                return None  # escape valve so we dont recures forever


# tests
unsolved = [[3, 0, 6, 0, 7, 8, 4, 9, 2],
            [5, 2, 9, 0, 0, 4, 7, 6, 0],
            [4, 8, 7, 0, 2, 9, 0, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [0, 0, 0, 8, 0, 3, 0, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 9, 2, 3, 0, 1, 8, 7, 4],
            [7, 0, 5, 2, 8, 6, 3, 1, 0]]

unsolved2 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]

printBoard(solve(unsolved))
printBoard(solve(unsolved2))
