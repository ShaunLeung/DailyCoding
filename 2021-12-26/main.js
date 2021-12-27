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
  if (n === 1) return array
  //first thing is to split the list in two
  var left = array.slice(0, n / 2)
  var right = array.slice(n / 2, n)
  var out = []
  var i = 0
  var j = 0
  left = mergeSort(left)
  right = mergeSort(right)

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      out.push(left[i])
      i++
    } else {
      out.push(right[j])
      j++
    }
  }
  for (; i < left.length; i++) out.push(left[i])
  for (; j < right.length; j++) out.push(right[j])

  return out
}

var array = [3, 2, 4, 5, 1]
console.log(mergeSort(array))
array = [3, 2, 4, 5, 1, 6]
console.log(mergeSort(array))
