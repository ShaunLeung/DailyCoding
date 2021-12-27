/**
 * Shaun Leung
 * Dec 27, 2021
 *
 * Almost caught up to the backlog of questions. This problem is interesting
 * because my instinct is to go towards the O(n^2) solution which is off the
 * table. I think if you do a sort and then a comparasin you can get it down to
 * n log n time, the problem I am having is structuring the comparasen so that
 * it doesnt end up being n^2. I might be able to count the inversions during
 * the sort like how I got a better running time with Dec 25's solution.
 */

const mergeSort = array => {
  n = array.length
  //base case
  if (n === 1) return [array, 0]
  //first thing is to split the list in two
  var left = array.slice(0, n / 2)
  var right = array.slice(n / 2, n)
  var out = []
  var i = 0
  var j = 0

  var [left, lm] = mergeSort(left)
  var [right, rm] = mergeSort(right)

  var misplaced = lm + rm

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      out.push(left[i])
      i++
    } else {
      out.push(right[j])
      j++
      misplaced += left.length - i //we know how many left items the right item is skipping and in constant time!!!!!
    }
  }
  for (; i < left.length; i++) out.push(left[i])
  for (; j < right.length; j++) out.push(right[j])

  return [out, misplaced]
}

const getInversions = array => {
  var [list, inversions] = mergeSort(array)
  return inversions
}
// Testing
var array = [2, 4, 1, 3, 5]
console.log(getInversions(array))
array = [5, 4, 3, 2, 1]
console.log(getInversions(array))
