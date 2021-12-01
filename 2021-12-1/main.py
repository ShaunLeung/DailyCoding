# Shaun Leung
# Dec 1, 2021

# Well this is a dynamic programing question if I have ever seen one
# since houses cant be the same colour in a row we will be considering the
# the next 2 houses and taking the cheapest path

# is the cheapest a valid grab option or do we need consider spending a bit more
# to get a discount later on.

# brute force is n^k... well a bit less b/c of the restriction so n * (n-1)^n-1
# still a lot

# We are going to find the cheapest cost k different ways so the time will be nk
# which is still shorter than brute force

# colour is the col index
# n is the row index...but we sort of ignore that

def minCost(matrix, n, k):
    # Create the specualtive array so that the current col is the colour we are
    # going to paint and we want the cheapest based on the previous houses we
    # have painted. We have to preload the array at the beginning because we
    # not painted any houses yet

    # initializing and preloading
    costMatrix = [[0 for i in range(n)] for j in range(k)]
    for colour, cost in enumerate(matrix[0]):
        costMatrix[0][colour] = cost

    # n+1 cause we take a slice
    for n, row in enumerate(matrix[1:]):
        for colour, cost in enumerate(row):
            costMatrix[n +
                       1][colour] = min(costMatrix[n][:colour]+costMatrix[n][colour+1:]) + cost

    return min(costMatrix[-1])


# Testing
costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
n = len(costs)
k = len(costs[0])
print(costs)
print(minCost(costs, n, k))

print()
costs = [[1, 2, 3, 4], [1, 2, 1, 0], [6, 1, 1, 5], [2, 3, 5, 5]]
n = len(costs)
k = len(costs[0])
print(costs)
print(minCost(costs, n, k))
