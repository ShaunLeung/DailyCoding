# Shaun Leung
# Dec 13, 2021

# This is a pretty classic problem.
# Surprisingly I have seen this problem before but it was in bioinformatics
# where you might want to compare two genomes (essentially really long strings)
# and see how large the edit distance is.


def editDistance(stringOne, stringTwo, matrix=[], m=0, n=0):
    if len(matrix) == 0:

        # initializing the matrix
        matrix = [[-1 for i in range(len(stringTwo)+1)]
                  for j in range(len(stringOne)+1)]
        # we know that the edit distance between a string and an empty string
        # is just the length of the non-empty string
        matrix[m][n] = 0
        for i in range(len(matrix)):
            matrix[i][0] = i
        for i in range(len(matrix[0])):
            matrix[0][i] = i

        m = len(stringOne)
        n = len(stringTwo)

    # if matching
    if stringOne[m-1] == stringTwo[n-1]:

        # check to see if we have calculated it yet
        if matrix[m-1][n-1] < 0:
            matrix[m][n] = editDistance(stringOne, stringTwo, matrix, m-1, n-1)
        else:
            matrix[m][n] = matrix[m-1][n-1]
    # time to do some editiing
    else:
        # if we have the values already great!
        ins = matrix[m-1][n]
        delete = matrix[m][n-1]
        swap = matrix[m-1][n-1]
        # if not we need to do some work.
        # insertion
        if ins < 0:
            ins = editDistance(stringOne, stringTwo, matrix, m-1, n)
        # deletion
        if delete < 0:
            delete = editDistance(stringOne, stringTwo, matrix, m, n-1)
        # swap
        if swap < 0:
            swap = editDistance(stringOne, stringTwo, matrix, m-1, n-1)

        matrix[m][n] = min(ins, delete, swap) + 1

    return matrix[m][n]


stringOne = 'This'
stringTwo = 'That'
print(stringOne)
print(stringTwo)
print("edit distance is = " + str(editDistance(stringOne, stringTwo)))
print()


stringOne = 'kitten'
stringTwo = 'sitting'
print(stringOne)
print(stringTwo)
print("edit distance is = " + str(editDistance(stringOne, stringTwo)))
print()
