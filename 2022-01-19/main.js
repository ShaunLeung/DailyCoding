//Shaun  Leung
/// Jan 20, 2022

/**
 * This is a pretty simple problem in that you just need to consider the bishops  that are further down on the board.
 */

/**
 * Created the game board of size MxM and populates it with bishops
 *
 * @param {*} bishops
 * @param {*} m
 * @returns {[[char]]} board
 */
const buildBoard = (bishops, m) => {
  const board = [[]]
  for (var i = 0; i < m; i++) {
    rank = []
    for (var j = 0; j < m; j++) {
      rank.push('_')
    }
    board[i] = rank
  }

  // add the bishops
  for (var i = 0; i < bishops.length; i++)
    board[bishops[i][0]][bishops[i][1]] = 'B'

  return board
}

/**
 * Checks the attacks that the bishop param can make further down the board.
 * @param {*} bishop the position of the bishop in question
 * @param {*} board
 * @returns {int} The number of attacks that bishop is making further down the board
 */
const checkDiag = (bishop, board) => {
  var left = bishop[1] - 1
  var right = bishop[1] + 1
  var attacks = 0
  for (var i = bishop[0] + 1; i < board.length; i++, left--, right++) {
    if (left >= 0) {
      if (board[i][left] == 'B') {
        attacks++
      }
    }
    if (right < board.length) {
      if (board[i][right] == 'B') {
        attacks++
      }
    }
  }
  return attacks
}
/**
 *  Combines the two previous functions to build the board and then to check
 * the list of bishops of attacks.
 *
 * @param {*} bishops A list of bishops
 * @param {*} m The size of the board
 * @returns {attacks} The number of attacks the bishops are making on the board
 */
const bishopAttacks = (bishops, m) => {
  const board = buildBoard(bishops, m)
  for (var i = 0; i < m; i++) console.log(board[i])
  var attacks = 0
  for (var i = 0; i < bishops.length; i++)
    attacks += checkDiag(bishops[i], board)
  console.log(attacks)
  return attacks
}

//Testing
const bishops = [
  [0, 0],
  [1, 2],
  [2, 2],
  [4, 0]
]
m = 5
console.log('There are ' + bishopAttacks(bishops, m) + ' attacks')
