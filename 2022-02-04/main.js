//Shaun Leung
//Feb 4, 2022

/**
 * This one seems pretty easy. I think it is a test to see if you are good at
 * picking out edge cases. At first I wanted to try and cut corner and
 * represent an island by a series of 4 values min/ max x/y but if there is a
 * "lake" on an island with its own island then the 4 values would miss it.
 *
 * Better be safe and just check every element.
 *
 * Going to need:
 * Function that checks neighbours, both orthagonal and diagonal.
 * Thought about making the function recursive but I think a simple
 * nested loop will be fine here.
 */

/**
 * Searches the Map for islands
 * @param {*} map
 * @returns # of islands
 */
const ahoy = map => {
  var islands = 0
  var n = map.length
  var m = map[0].length
  var found = new Array(n)
  for (var i = 0; i < n; i++) found[i] = new Array(m)
  // set the found map
  for (var i = 0; i < n; i++) {
    for (var j = 0; j < m; j++) found[i][j] = false
  }

  /**
   * Recursive function that goes through and marks off all the adjancent
   * elements that are also land.
   * @param {*} i y pos
   * @param {*} j x pos
   */
  const explore = (i, j) => {
    if (map[i][j] == 1 && found[i][j] == false) {
      found[i][j] = true

      if (i > 0 && j > 0) explore(i - 1, j - 1) //top left
      if (i > 0) explore(i - 1, j) //top mid
      if (i > 0 && j < m - 1) explore(i - 1, j + 1) //top right
      if (j < m - 1) explore(i, j + 1) //mid right
      if (i < n - 1 && j < m - 1) explore(i + 1, j + 1) //bot right
      if (i < n - 1) explore(i + 1, j) //bot mid
      if (i < n - 1 && j > 0) explore(i + 1, j - 1) //bot left
      if (j > 0) explore(i, j - 1) //mid left
    }
  }

  for (var i = 0; i < map.length; i++) {
    for (var j = 0; j < map[0].length; j++) {
      //miss
      if (map[i][j] == 1 && found[i][j] == false) {
        islands++
        explore(i, j)
      }
      //hit
      else if (map[i][j] == 0) {
        found[i][j] = true
      }
    }
  }
  return islands
}

//Testing
map = [
  [1, 0, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [1, 1, 0, 0, 1],
  [1, 1, 0, 0, 1]
]

console.log(ahoy(map))

//Edge case test
caldera = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1]
]

console.log(ahoy(caldera))
