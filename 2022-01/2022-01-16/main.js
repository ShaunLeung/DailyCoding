//Shaun Leung
// Jan 17, 2022

/**
 * This challenge seems easy enough and I think its to see how elegant the
 * code can be.
 */

const clockwise = matrix => {
  var top = 0
  var right = matrix[0].length
  var bottom = matrix.length
  var left = 0

  while (top < bottom && left < right) {
    ///top
    for (var i = left; i < right; i++) console.log(matrix[top][i])
    top++

    //right
    for (var i = top; i < bottom; i++) console.log(matrix[i][right - 1])
    right--

    //bottom
    for (var i = right - 1; i >= left; i--) console.log(matrix[bottom - 1][i])
    bottom--

    //left
    for (var i = bottom - 1; i >= top; i--) console.log(matrix[i][left])
    left++
  }
}

array = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
]

clockwise(array)

array = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30]
]

clockwise(array)
