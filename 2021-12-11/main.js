/**
 * Shaun Leung
 * Dec 11, 2021
 *
 * This question seems pretty straight forward. Can just walk through the loop
 * keep track of how many of a new character we have seen and then append to a
 * new output string.
 *
 * Looks like I also need to do the decoding as well which shouldnt bee too bad
 */

const rlEncoding = string => {
  const outString = []
  //preload the counters
  var num = 1
  var char = string[0]
  for (var i = 1; i < string.length; i++) {
    //new char so update var and record old
    if (string[i] != char) {
      outString.push(num)
      outString.push(char)
      char = string[i]
      num = 1
    } else num++
  }
  //add the last
  outString.push(num)
  outString.push(char)
  return outString.join('')
}

const rlDecoding = string => {
  //we know it starts with a num and aternates to char
  var num = string[0]
  var char = string[1]
  outString = []

  for (var i = 2; i <= string.length; i += 2) {
    for (var j = 0; j < num; j++) outString.push(char)
    num = string[i]
    char = string[i + 1]
  }

  return outString.join('')
}

// testing
string = 'AAAABBBCCDAA'
console.log(string)
newString = rlEncoding(string)
console.log(newString)
console.log(rlDecoding(newString))
console.log(
  string +
    ' == ' +
    rlDecoding(newString) +
    ' = ' +
    (string === rlDecoding(newString))
)
