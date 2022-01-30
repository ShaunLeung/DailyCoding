// Shaun Leung
//Jan 30, 2022

/**
 * This one actually seems pretty easy, the term "non-decreasing" kind of threw
 * me for a second but I think all it means is that you can have sequential ints
 * of the same value.
 *
 * The other thing that needs to be check is if we run into a second value that
 * violates the above rule. I think a simple flag will be able to do the trick
 * here.
 *
 * Also the question only mentiones that it is an int array which means that
 * negative numbers are available so we dont have to be worried about running
 * up against zero.
 */

const nonDecreassing = array => {
  if (array.length === 0) return true

  var flag = false
  var cur = array[0]

  for (var i = 1; i < array.length; i++) {
    if (cur > array[i]) {
      if (flag === false) flag = true
      else return false
    }
    cur = array[i]
  }
  return true
}

//Testing
var array = [10, 5, 7]
console.log(array)
console.log(nonDecreassing(array))
array = [10, 5, 1]
console.log(array)
console.log(nonDecreassing(array))
