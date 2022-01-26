# Shaun Leung
# Jan 26, 2022

"""
This is very clearly a dynamic programing  question but the problem I am having
with it is the constraints with whether to take a number or not. Seem like there
is no good rule to follow for that. I then thought if backtracking would work, 
but there is no definitive fail case to stop, back up and try again so that idea
is not it. 

Could always brute force it but that makes it a little to slow. 

Alright had to look this one up and I was close in that it is dynamic 
programming but not exactly how I thought it would work. 

Also I really need to read the question more carefully because I only need to
return the length of the sub array and not the array itself. 

Turns out the answer is pretty similar to the edit distance problem
"""


def lis(array):
    sorted = list(array)
    sorted.sort()

    matrix = [[-1 for _ in range(len(array)+1)] for _ in range(len(array)+1)]

    for i in range(len(array)+1):
        for j in range(len(array)+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif array[i-1] == sorted[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

    return matrix[-1][-1]


array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(array)
print("Longest Increasing Subarray:", lis(array))
