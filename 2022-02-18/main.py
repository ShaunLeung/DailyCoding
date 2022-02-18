# Shaun Leung
# Feb 18, 2022

"""
This one took me a second to understand in that I thought it was a word search
at first but as it turns out it is actually more like a maze as the word can 
take twists and turns (orthagonally) through the board. 

Since it is a pathing thing I think back tracking is probably the best solution.
pick a path and go down it until you run into an issue. 
"""

def exists(board,word):
    """
    Takes in a 2d array of char and a word. Trys to find the word in the board
    of characters. 

    @Param{[String]}    A game board of a list of strings
    @Param{String}      The word to be found in the board
    @Return{Boolean}    True if the word exits, false otherwise
    """
    maxX = len(board[0])-1
    maxY = len(board)-1
    exists = False

    used = [[False for _ in range(maxX+1)] for _ in range(maxY+1)]

    def path(pos, word):
        """
        Paths, recursively, through the board only going down valid paths and backtracks
        if neccisary

        Note: that it assumes the first case is valid. 
        
        @Param{(int,int)}   (X,Y) position of the chard being looked at on 
                            board
        @Param{String}      The word that is trying to be matched
        @Return{Boolean}    Returns True if the word is in the board and
                            False otherwise. 
        """
        #Used up all the letters!
        if len(word) == 0:
            return True

        x,y = pos
        # check orthagonal directions
        if y >-1:
            if board[y-1][x] == word[0] and not used[y-1][x]:
                used[y-1][x] = True
                return path((x,y-1),word[1:])
        
        if x < maxX:
            if board[y][x+1] == word[0] and not used[y][x+1]:
                used[y][x+1] = True
                return path((x+1,y),word[1:])
        
        if y < maxY:
            if board[y+1][x] == word[0] and not used[y+1][x]:
                used[y+1][x] = True
                return path((x,y+1),word[1:])

        if x >-1:
            if board[y][x-1] == word[0] and not used[y][x-1]:
                used[y][x-1] = True
                return path((x-1,y),word[1:])
        
        # no more paths 
        used[y][x] = False # Revert
        return False


    # go through the possible starting locations
    for y,row in enumerate(board):
        for x, item in enumerate(row):
            if item == word[0] and not exists: # stop checking when found
                exists = path((x,y), word[1:])

    return exists



# Testing
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(exists(board, "ABCCED"))
print(exists(board, "ABCCED"))
print(exists(board, "ABCB"))


"""
Got most of it coded but forgot one small thing about not being able to resuse
letters that have been previously used before. Not to bad of an addition.
"""