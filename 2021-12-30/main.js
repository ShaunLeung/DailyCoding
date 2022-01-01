/**
 * Shaun Leung
 * Jan 1, 2022
    
This problem is pretty clearly a dynamic programing question. 
at first I was thinking of using 2d memoization to solve the problem but the 
time complexity restriction prevents that since it would be longer than O(N)

what can be done though is to compare running totals to the max updating each 
for each element examened.
 */

const maxSub = array => {
  const n = array.length
  //preload the array
  var outMax = array[0]
  var runMax = array[0]

  for (var i = 1; i < n; i++) {
    outMax = Math.max(array[i], outMax + array[i])
    runMax = Math.max(outMax, runMax)
  }
  //need to account for taking no items
  if (outMax < 0) return 0
  return outMax
}

//testing
array = [34, -50, 42, 14, -5, 86]
console.log(maxSub(array))

array = [-5, -1, -8, -9]
console.log(maxSub(array))
