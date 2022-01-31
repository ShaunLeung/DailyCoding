// Shaun Leung
// Jan 25, 2022

/**
 * This one actually seems a little too easy and I wonder if there is a trick
 * that I am missing.
 *
 * The straight forward was would to be just check every index of the 2d array
 * and increment when you encounter X. Looking at the example in the question
 * you can see that the graph is mirored on its diagonal so really you only need
 * to go through haalf the 2d array and then just multiply the result by 2.
 */

const findX = (n, x) => {
  var hit = 0
  for (var i = 1; i <= n; i++) for (var j = 1; j < i; j++) if (i * j == x) hit++

  for (var i = 1; i <= n; i++) if (i * i == x) hit++
  return hit * 2
}

//Testsint
var x = 24
var n = 6
console.log(findX(n, x))

x = 12
console.log(findX(n, x))

x = 19 //prime # should return 0 if < n
console.log(findX(n, x))
