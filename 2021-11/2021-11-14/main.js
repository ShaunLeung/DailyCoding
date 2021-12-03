/**
 * Shaun Leung
 * Dec 2, 2021
 *
 * I am revisiting this question since I think I can do it better and with the
 * additional challenge of not using the division operator.
 *
 * To do this withought using the division operator you need to use dynamic
 * programing twice.
 *
 * You need to build an array that keeps track of the
 * products for itself and all numbers that have come before so for an array
 * of [1,2,3] it would be [1,2,6]
 *
 * You also need to do this for the reverse as well [1,2,3] would be [6,6,3]
 *
 * Also I am doing this in js because I can feel myself getting a little rusty
 */

const otherProducts = array => {
  // getting the value of n because I find it tedious getting length often
  const n = array.length

  // array with a running total of the product before and including the index
  const preProduct = []
  preProduct[0] = array[0]
  for (let i = 1; i < n; i++) preProduct[i] = preProduct[i - 1] * array[i]

  // array with a running total of the product after and including the index
  const postProduct = []
  postProduct[n - 1] = array[n - 1]
  for (let i = n - 2; i >= 0; i--)
    postProduct[i] = postProduct[i + 1] * array[i]

  // build the product array
  const product = []
  //cheating by loading the first and the last since they are easy
  product[0] = postProduct[1]
  product[n - 1] = preProduct[n - 2]
  for (let i = 1; i < n - 1; i++)
    product[i] = preProduct[i - 1] * postProduct[i + 1]

  return product
}

// Testing
testArray = [1, 2, 3, 4, 5]
console.log(testArray)
console.log(otherProducts(testArray))
console.log('*********************')

testArray = [3, 2, 1]
console.log(testArray)
console.log(otherProducts(testArray))
console.log('*********************')

// one zero
testArray = [0, 2, 3, 4, 5]
console.log(testArray)
console.log(otherProducts(testArray))
console.log('*********************')

// two zeroes
testArray = [0, 2, 3, 4, 0]
console.log(testArray)
console.log(otherProducts(testArray))
console.log('*********************')

// one negative
testArray = [-1, 2, 3, 4, 5]
console.log(testArray)
console.log(otherProducts(testArray))
console.log('*********************')

// two negative
testArray = [-1, 2, 3, 4, -5]
console.log(testArray)
console.log(otherProducts(testArray))
console.log('*********************')
