# Shaun Leung
# Dec 5, 2021

# going to try some memoizaton for this one and generate a grid of weights
# Note: can only move orthagnonaly.

def findShortest(map, start, end):
    height = len(map)
    width = len(map[0])
    cur = start

    # initialize the weighted grid
    memo = [[float('inf') for i in range(width)]for j in range(height)]
    memo[cur[0]][cur[1]] = 0

    # pre load moves
    moves = []
    addMoves(cur, moves, memo)

    # get next moves
    while moves != []:
        cur = moves.pop(0)
        if cur == end:
            return "Finished " + str(memo[cur[0]][cur[1]])
        addMoves(cur, moves, memo)

    return "No Solution"


def isValid(cur, map):
    height, width = len(map), len(map[0])
    y, x = cur[0], cur[1]
    return x >= 0 and y >= 0 and x < width and y < height and not map[y][x]


def addMoves(cur, moves, memo):
    up = (cur[0]-1, cur[1])
    right = (cur[0], cur[1]+1)
    down = (cur[0]+1, cur[1])
    left = (cur[0], cur[1]-1)
    if isValid(up, map) and memo[up[0]][up[1]] > memo[cur[0]][cur[1]]:
        moves.insert(0, up)
        memo[up[0]][up[1]] = memo[cur[0]][cur[1]] + 1
    if isValid(right, map) and memo[right[0]][right[1]] > memo[cur[0]][cur[1]]:
        moves.insert(0, right)
        memo[right[0]][right[1]] = memo[cur[0]][cur[1]] + 1
    if isValid(down, map) and memo[down[0]][down[1]] > memo[cur[0]][cur[1]]:
        moves.insert(0, down)
        memo[down[0]][down[1]] = memo[cur[0]][cur[1]] + 1
    if isValid(left, map) and memo[left[0]][left[1]] > memo[cur[0]][cur[1]]:
        moves.insert(0, left)
        memo[left[0]][left[1]] = memo[cur[0]][cur[1]] + 1


map = [[False, False, False, False],
       [True, True, False, True],
       [False, False, False, False],
       [False, False, False, False]]

print(findShortest(map, (3, 0), (0, 0)))
