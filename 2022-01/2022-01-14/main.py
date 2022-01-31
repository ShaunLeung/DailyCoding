# Shaun Leung
# Jan 14, 2022

"""
Gonna make a small assumption that the matrix is of even length and size of the
word that is being searched for. 

If I have enough time after I will try different sized matrixes and where the
word doesnt ntted to be at the start. 
"""


def wordSearch(matrix, word):
    """
    This was a fun function to write. I nested some helper functions inside so
    that variables would already be in scope. Also the helper function make use
    of the fact that negative indexes look at the tail of the array so that way 
    I don't need to worrk about bounds checking b/c I already know I want to 
    search the whole string.

    This function searches the Diagonal of the matrix. 

    :Param matrix:  The 2D array that may contain the word
    :Param word:    The word that is being searched for
    :Return Boolean: True if the matrix contains the word, False otherwise.  
    """
    x = 0
    y = 0
    n = len(word)

    def searchAcross():
        i = x
        for _ in range(n):
            if matrix[y][i] != word[i]:
                return False
            i -= 1
        return True

    def searchDown():
        i = y
        for _ in range(n):
            if matrix[i][x] != word[i]:
                return False
            i -= 1
        return True

    while x < n:
        if matrix[y][x] == word[x]:
            if searchAcross():
                return True
            if searchDown():
                return True
        x += 1
        y += 1

    return False


# Testing

matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]

for line in matrix:
    print(line)

word = 'FOAM'
print(word)
print("Is", word, "in the matrix: ", wordSearch(matrix, word))

word = 'MASS'
print("Is", word, "in the matrix: ", wordSearch(matrix, word))

word = 'LIKE'
print("Is", word, "in the matrix: ", wordSearch(matrix, word))
