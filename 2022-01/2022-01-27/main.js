// Shaun Leung
// Jan 27, 2022

/**
 * So I thought this question was much harder than it actually is. Ver simply
 * all we have to do is go row by row and count how many columns need to be
 * removed, you dont actually have to remove them, and since all the char
 * are lower case we dont have to worry about  capitals so we can do direct
 * comparasons.
 */

const lexico = matrix => {
  var removed = 0
  for (var i = 0, last = '`'; i < matrix[0].length; i++, last = '`')
    for (var j = 0; j < matrix.length; j++)
      if (last > matrix[j][i]) {
        removed++
        break
      } else last = matrix[j][i]

  return removed
}

var matrix = [
  ['c', 'b', 'a'],
  ['d', 'a', 'f'],
  ['g', 'h', 'i']
]
console.log(matrix)
console.log(lexico(matrix))

matrix = ['abcdef']
console.log(matrix)
console.log(lexico(matrix))

matrix = [
  ['a', 'y', 'x'],
  ['w', 'v', 'u'],
  ['t', 's', 'r']
]
console.log(matrix)
console.log(lexico(matrix))
