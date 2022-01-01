/**
 * Shaun Leung
 * Jan 1, 2022
 *
 * Playing catchup a little bit but this one seems to be pretty simple
 *
 * This problem looks to be a dynamic programming question.
 */

const priceMax = array => {
  const n = array.length
  const maxList = new Array(n)

  var buyIndex = 0
  for (var i = 0; i < n; i++) {
    //check if the current index is lower and we should buy
    if (array[i] < array[buyIndex]) buyIndex = i
    // we buy and sell the same day since that is all we can do profit is 0
    if (i == 0) maxList[i] = 0
    //check to see if we can make more money than the day before
    else if (array[i] - array[buyIndex] > maxList[i - 1])
      maxList[i] = array[i] - array[buyIndex]
    //if not carry on best from the previous day
    else maxList[i] = maxList[i - 1]
  }
  return maxList[n - 1]
}

//testing
array = [9, 11, 8, 5, 7, 10]
console.log(array)
console.log(priceMax(array))
