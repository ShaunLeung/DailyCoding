/**
 * Shaun Leung
 * Dec 28, 2021
 *
 * This question is labled as hard so there is probabaly a trick to it.
 * I think for the first stab at this without looking up any hints I am
 * goin to try and solve it brute force and then look for areas where I
 * can streamline things.
 *
 * base info is that a palindrom is a set or letters that are the same in
 * reverse order. that means is i is the index at the start and j is the index
 * at the end I need to compare the two then increment and decrement
 * resepectively until the i==j
 *
 * Since I need to find the longest palindrom in the string I will need to check
 * each index to see if it is the start of the longest ( or one of the longest)
 * I can already start to see ways to streamline this such as not having to
 * check the last index if the string is >1 since I only need to return one
 * palindrom and the simplest palindrome is just a single letter.
 */

const subPal = string => {
  longest = ''
  //check each letter as the start
  for (var i = 0; i < string.length; i++) {
    subI = i
    //check each index as the end
    for (subJ = string.length; subI < subJ; subJ--) {
      subSubI = subI
      subSubJ = subJ
      //check if the start and end make a palindrome
      for (; subSubI < subSubJ; subSubI++, subSubJ--)
        if (string[subSubI] != string[subSubJ]) break

      //palindrome was found so we record it
      if (
        subSubI >= subSubJ &&
        string.slice(subI, subJ + 1).length > longest.length
      )
        longest = string.slice(subI, subJ + 1)
    }
  }
  return longest
}

//Testing
string = 'aabbcdcb'
console.log(string)
console.log(subPal(string) + '\n')

string = 'bananas'
console.log(string)
console.log(subPal(string) + '\n')

/**
 * Alright the brute force way works but I think it can be made a little better
 * since we are checking some substrings that wont be viable just because of
 * size requirements of what has already been found.
 *
 * next function will ignore substrings that are already shorter than the
 * longest
 */

const subPal2 = string => {
  longest = ''
  //check each letter as the start
  for (var i = 0; i < string.length - longest.length; i++) {
    subI = i
    //check each index as the end
    for (subJ = string.length; subI + longest.length < subJ; subJ--) {
      subSubI = subI
      subSubJ = subJ
      //check if the start and end make a palindrome
      for (; subSubI < subSubJ; subSubI++, subSubJ--)
        if (string[subSubI] != string[subSubJ]) break

      //palindrome was found so we record it
      if (
        subSubI >= subSubJ &&
        string.slice(subI, subJ + 1).length > longest.length
      )
        longest = string.slice(subI, subJ + 1)
    }
  }
  return longest
}

//Testing
string = 'aabbcdcb'
console.log('Function 2 check')
console.log(string)
console.log(subPal2(string) + '\n')

string = 'bananas'
console.log(string)
console.log(subPal2(string) + '\n')

/**
 * Now triple nested loops are never great for time complexity
 * but since there was no time complexity given for this challenge
 * I am gonna count this as a win.
 */
