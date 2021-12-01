# Shaun Leung
# Nov 14, 2021

# Easist way to solve this is to get the product of each number in the array
# and then divide by the current element essentially removing its contribution
# to the product.
#
# An edge case to watch out for is if an element has a value of 0 since you
# cannot divide by 0 and that element's index in the reutrned array would be a
# non-zero number.
#
# zeroes can be "ignored" and treaded as ones on a seperate signma function if
# a zero is found in the original list since we then know that all other
# elements of the returned list should be 0 and the index with a 0 will be the
# product.
#
# One last issue is if there are two indexes with a value of zero which means
# the entire returned list should be zero.
#
# First check for zeroes
# if zeroes >1 return list of same length full of zerros
# if zeroes =1 return list of zeroes, index of zero will be product
# if zerroes =0 find sigma of list and then make new list by dividing out indexes

# Normal Sigma
def sigma(intArray):
    product = 1
    for num in intArray:
        product *= num
    return product

# Zero Controlled Sigma


def sigmaZero(intArray):
    product = 1
    for num in intArray:
        if num == 0:
            product *= 1
        else:
            product *= num
    return product

# find the zeroes


def findzeroes(intArray):
    zeroes = 0
    for num in intArray:
        if num == 0:
            zeroes += 1
    return zeroes

# replaceing each index with the product of other indexes


def otherProducts(intArray):
    productArray = []
    zeroes = findzeroes(intArray)
    if zeroes >= 2:
        return [0] * len(intArray)
    if zeroes == 1:
        product = sigmaZero(intArray)
        for num in intArray:
            if num == 0:
                productArray.append(product)
            else:
                productArray.append(0)
    else:
        product = sigma(intArray)
        for num in intArray:
            # This will always be an int but just for type saftey
            productArray.append(int(product/num))
    return productArray


# Testing
testArray = [1, 2, 3, 4, 5]
print(testArray)
print(otherProducts(testArray))
print('*********************')

testArray = [3, 2, 1]
print(testArray)
print(otherProducts(testArray))
print('*********************')

# one zero
testArray = [0, 2, 3, 4, 5]
print(testArray)
print(otherProducts(testArray))
print('*********************')

# two zeroes
testArray = [0, 2, 3, 4, 0]
print(testArray)
print(otherProducts(testArray))
print('*********************')

# one negative
testArray = [-1, 2, 3, 4, 5]
print(testArray)
print(otherProducts(testArray))
print('*********************')

# two negative
testArray = [-1, 2, 3, 4, -5]
print(testArray)
print(otherProducts(testArray))
print('*********************')
