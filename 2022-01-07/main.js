// Shaun Leung
// Jan 7, 2022

/**
 * This one actually feels pretty familiar from school, there were so many
 * graph questions. Since we dont need to return the graph and only a boolean
 * if it is possible or not we can do this nice and quick with a breadth first
 * search. Also we can double up and have the array indicating if a node has
 * been coloured be the array we use to see if the node has also been visited.
 *
 * Colours will be represented by ints 1-m, with 0 being reserved for
 * uncoloured
 */

/**
 * Utility Function
 * Checks the node in the matrix to make sure that any adjacent nodes aren't
 * the colour specified in the parameter
 *
 * @param {*} matrix    Adjacency Matrix
 * @param {*} node      Node to check
 * @param {*} coloured  List of nodes and their colours, also visited.
 * @param {*} c         potential colour
 * @returns {boolean}   True if the node can be coloured c, false otherwise
 */
const isValid = (matrix, node, coloured, c) => {
  for (var i = 0; i < matrix.length; i++)
    if (matrix[node][i] === 1 && coloured[i] === c) return false

  return true
}
/**
 * Thought about doing this function recursively but I have done that a lot
 * lately so I am just going to toss it in a while loop that runs while there
 * node to be coloured
 *
 * @param {*} matrix    Adjacency matrix that represents a graph
 * @param {*} m         Number of colours we have to work with
 * @returns {boolean}   True if it the graph can be coloured with at least m
 *                      colours, false otherwise
 */
const canBeColoured = (matrix, m) => {
  //initialize coloured array
  var coloured = []
  for (var i = 0; i < matrix.length; i++) coloured.push(0)
  var search = [] // list of nodes to search through
  search.push(0) //start with the first node

  while (search.length > 0) {
    node = search.shift()
    //cycle through the possible colours
    var c = 1 // awk to have this our of scope but I want to check it later
    for (; c < m + 1; c++) {
      if (isValid(matrix, node, coloured, c)) {
        coloured[node] = c //colour the node
        //add neighbours not visited
        for (var i = 0; i < matrix.length; i++) {
          if (coloured[i] === 0 && matrix[node][i] === 1) search.push(i)
        }
        break //able to colour so we can stop looking
      }
    }
    if (c > m) return false //Cant colour the node
  }
  return true
}

v2 = [
  [1, 1],
  [1, 1]
]

//should return false on m = 1 and true one m > 1

for (var i = 0; i < v2.length; i++) console.log(v2[i])
console.log('m = 1: ' + canBeColoured(v2, 1))
console.log('m = 2: ' + canBeColoured(v2, 2))

graph = [
  [0, 1, 1, 1],
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [1, 0, 1, 0]
]

for (var i = 0; i < graph.length; i++) console.log(graph[i])
console.log('m = 2: ' + canBeColoured(graph, 2))
console.log('m = 4: ' + canBeColoured(graph, 4))

/**
 * After finishing this it actually would be pretty easy to return the colour
 * assignments since it is simply stored in the coloured array.
 *
 * In retrospective this probably could have been done a lot clearner as a
 * recursive function. Maybe I will come back to it in the future.
 */
