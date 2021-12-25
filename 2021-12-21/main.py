# Shaun Leung
# Dec 24, 2021

"""
This one doesn't seem too diffcult as it can be broken down into a couple of
problems

The first problem is dealing with the infinite board. we can start with board
and then increase it if we have a living cell expanding the board. Doing it on the bottom or the right is not a huge deal but the left on top will require some
index shifting.
    -I am not a fan of coding bounds checking which is why this seems the most
    onerous to me

A smaller problem is that there needs to be neighbour checking. Which includes
diagonals.

Things to code:
Board expansion
    -left
    -right
    -top
    -bottom
    -cell shifting

neighbour checking
    -verticle
    -horizontal
    -diagonal

Rules
    -live
        <2 die
        2-3 live
        >3 die
    - dead
        =3 live
            -check in range
            -check out of range
"""

import copy
"""
Creates the initial board state based on the cells that have been added.
"""


def boardInit(cells):
    x, y = zip(*cells)
    maxX = max(x)
    maxY = max(y)

    width = maxX+1
    height = maxY+1
    board = [['.' for i in range(width)] for j in range(height)]

    for cell in cells:
        board[cell[1]][cell[0]] = 'X'

    return board


"""
Checking the neighbours of each cell one by one cant use try because
there is now out of bounds at negative, it grabs tail
"""


def neighbours(board, cell):
    alive = 0
    dead = 0
    j, i = cell
    # going clockwise from the top left
    if i > 0 and j > 0:
        if board[i-1][j-1] == 'X':
            alive += 1

        else:
            dead += 1
    else:
        dead += 1

    if i > 0:
        if board[i-1][j] == 'X':
            alive += 1

        else:
            dead += 1
    else:
        dead += 1

    if i > 0 and j < len(board[i])-1:
        if board[i-1][j+1] == 'X':
            alive += 1

        else:
            dead += 1
    else:
        dead += 1

    if j < len(board[i])-1:
        if board[i][j+1] == 'X':
            alive += 1

        else:
            dead += 1
    else:
        dead += 1

    if i < len(board)-1 and j < len(board[i])-1:
        if board[i+1][j+1] == 'X':
            alive += 1

        else:
            dead += 1
    else:
        dead += 1

    if i < len(board)-1:
        if board[i+1][j] == 'X':
            alive += 1

        else:
            dead += 1
    else:
        dead += 1

    if i < len(board)-1 and j > 0:
        if board[i+1][j-1] == 'X':
            alive += 1

        else:
            dead += 1
    else:
        dead += 1

    if j > 0:
        if board[i][j-1] == 'X':
            alive += 1

        else:
            dead += 1
    else:
        dead += 1

    return alive, dead


def rules(board, cells):
    newBoard = copy.deepcopy(board)
    zombies = []

    # check living cells
    for cell in cells:
        live, dead = neighbours(board, cell)
        if live < 2:
            zombies.append(cell)
        if live > 3:
            zombies.append(cell)
    # check dead
        # going to break this down into 2 sections
        # 1: if a new row or col needs to be added
            # dont need to worry about corners
            # (this is where minesweaper skills come in handy)
            # need to check the neighbours of cell hits
            # -left and right for top and bottom
            # up and down for left and right
            # will have to worry about shifting
        # 2: if it is a dead cell in the board already then the neightbours
        # funtion can take care of it.

    # note these are indices
    maxY = len(board) - 1
    maxX = len(board[0]) - 1

    babies = []
    # check inside
    for i in range(maxY+1):
        for j in range(maxX+1):
            if board[i][j] == '.':
                live, dead = neighbours(board, (j, i))
                if live == 3:
                    babies.append((j, i))

    # check edges
    shiftDown = False
    shiftLeft = False
    shiftUp = False
    shiftRight = False
    # top check
    for i, cell in enumerate(board[0]):
        if cell == 'X':
            if i != 0 and i != maxX:
                if board[0][i-1] == 'X' and board[0][i+1] == 'X':
                    shiftDown = True
                    # shifted after the board is adjusted
                    babies.append((i, -1))

    # right check
    for i, cell in enumerate(board):
        if cell[maxX] == 'X':
            if i != 0 and i != maxY:
                if board[i-1][maxX] == 'X' and board[i+1][maxX] == 'X':
                    shiftLeft = True
                    babies.append((maxX+1, i))

    # bottom check
    for i, cell in enumerate(board[maxY]):
        if cell == 'X':
            if i != 0 and i != maxX:
                if board[maxY][i-1] == 'X' and board[maxY][i-1] == 'X':
                    shiftUp = True
                    babies.append((i, maxY+1))

    # left check
    for i, cell in enumerate(board):
        if cell[0] == 'X':
            if i != 0 and i != maxY:
                if board[i-1][0] == 'X' and board[i+1][0] == 'X':
                    shiftRight = True
                    babies.append((-1, i))

    # adding rows and cols to the board if need be
    if shiftDown:
        newRow = ['.' for _ in range(maxX+1)]
        newBoard.insert(0, newRow)
        # shift all cells of note down one
        newCells = []
        for cell in cells:
            tCell = list(cell)
            tCell[1] += 1
            newCells.append(tuple(tCell))
        cells = newCells

        newCells = []
        for cell in zombies:
            tCell = list(cell)
            tCell[1] += 1
            newCells.append(tuple(tCell))
        zombies = newCells

        newCells = []
        for cell in babies:
            tCell = list(cell)
            tCell[1] += 1
            newCells.append(tuple(tCell))
        babies = newCells

    if shiftLeft:
        for row in newBoard:
            row.append('.')

    if shiftUp:
        newRow = ['.' for _ in range(maxX+1)]
        newBoard.append(newRow)

    if shiftRight:
        for row in newBoard:
            row.insert(0, '.')
        # shit all cells of note right one
        newCells = []
        for cell in cells:
            tCell = list(cell)
            tCell[0] += 1
            newCells.append(tuple(tCell))
        cells = newCells

        newCells = []
        for cell in zombies:
            tCell = list(cell)
            tCell[0] += 1
            newCells.append(tuple(tCell))
        zombies = newCells

        newCells = []
        for cell in babies:
            tCell = list(cell)
            tCell[0] += 1
            newCells.append(tuple(tCell))
        babies = newCells

    # add new and dying cells to newBoard and cells

    for cell in zombies:
        newBoard[cell[1]][cell[0]] = '.'
        cells.remove(cell)

    for cell in babies:
        newBoard[cell[1]][cell[0]] = 'X'
        cells.append(cell)

    return newBoard, cells


def printBoard(board, cells=None):
    if not cells and len(cells) != 0:
        for i in board:
            print(i)
        for _ in range(len(board[0])*5 + 2):
            print('-', end='')
        print()
    else:
        if not cells:
            print("Game Over")
            return False
        x, y = zip(*cells)
        maxX = max(x)
        maxY = max(y)
        minX = min(x)
        minY = min(y)

        while minY <= maxY:
            minX = min(x)
            while minX <= maxX:
                print(board[minY][minX], end='')
                minX += 1
            minY += 1
            print()
        print('_________________')
    return True


def gameOfLife(cells, tics):
    board = boardInit(cells)
    printBoard(board, cells)
    for _ in range(tics):
        board, cells = rules(board, cells)
        if not printBoard(board, cells):
            break


# testing
# output will transpose each rotation
#cells = [(1, 0), (2, 0), (0, 0) ]

cells = [(1, 0), (2, 0), (0, 0), (9, 0), (9, 2),
         (9, 1)]
gameOfLife(cells, 5)
