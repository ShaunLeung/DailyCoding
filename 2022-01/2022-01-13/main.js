//Shaun Leung
// Jan 13, 2022
/**
 * The question seems easy enough and I think the challenge is in writting a
 * recursive program to traverse through the matrix since that is more often
 * done with loops. It also looks like the function is not passes the matrix
 * itself but rather its lengths.
 *
 * Just need to go recursively go through the matrix and watch out for bound
 * with the base case being return 1 for the node being looked at. There are
 * only 2 recursive moves since we can only increase i or j and not both.
 */

/**
 * Recursive function that recursively goes through the matrix until i and j are
 * eqaul to n and m. At most there are two possible moves for any specific
 * position. Since we are finding paths the result will be equal to or greater
 * to the product of M and N
 *
 * @param {*} n height of the array
 * @param {*} m length of the array
 * @param {*} i current pos in height
 * @param {*} j current pos in length
 * @returns the sum of itself and next nodes
 */
const matrixRecurse = (n, m, i = 0, j = 0) => {
  //basecase
  if (i === n - 1 && j === m - 1) return 1

  //recursive step
  var sum = 0
  if (i < n) {
    sum += matrixRecurse(n, m, i + 1, j)
  }
  if (j < m) sum += matrixRecurse(n, m, i, j + 1)
  return sum
}
//testing
n = 2
m = 2
a = Array(n)
  .fill(0)
  .map(x => Array(m).fill(0))

for (var i = 0; i < a[0].length; i++) console.log(a[i])
console.log('There are ' + matrixRecurse(a.length, a[0].length) + ' paths')

n = 5
m = 5
a = Array(n)
  .fill(0)
  .map(x => Array(m).fill(0))

for (var i = 0; i < a[0].length; i++) console.log(a[i])
console.log('There are ' + matrixRecurse(a.length, a[0].length) + ' paths')
