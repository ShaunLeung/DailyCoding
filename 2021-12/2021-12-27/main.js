/**
 * Shaun Leung
 * Dec 27, 2021
 *
 * Finally back on track
 *
 * Alright this one is tagged as easy and it is!
 * This is a pretty mathy challenge but the math itself isnt too bad
 * You reall just need to find the loweset common denominator between 7 and 5,
 *  technically and common denominator will work but we'll use 35 for this one.
 */

const rand5 = () => {
  return Math.floor(Math.random() * 7) + 1
}

const rand7 = () => {
  num = rand5() * 10 + rand5()
  return (num % 7) + 1
}

const std = array => {
  return Math.sqrt(array.reduce((sum, item) => (sum += item)) / array.length)
}

//testing
const itter = 7000
const tally = [0, 0, 0, 0, 0, 0, 0]
const sums = []
for (var i = 0; i < itter; i++) {
  var num = rand7()
  tally[num - 1]++
  sums.push(num)
}

console.log(tally)

//sanity check that rand7 is just as uniform as rand5
console.log('Standard Deviations')
console.log('Rand7: ' + std(sums))
const sums5 = []

for (var i = 0; i < itter; i++) {
  var num = rand5()
  sums5.push(num)
}
console.log('Rand5: ' + std(sums5))

//checking the avg
console.log('Averages')
console.log('Rand7: ' + sums.reduce((sum, item) => (sum += item)) / sums.length)
console.log(
  'Rand5: ' + sums5.reduce((sum, item) => (sum += item)) / sums5.length
)
/**
 * Alright had a bit of hubris with this one and it wasent as easy as I thought
 * Tried doing a sum of 2 rand5 and then re-rolling for numbers out of bounds
 * but I forgot that summing the numbers changes the balancing like with 2d6
 * a 7 is more likely to be rolled than a 12 or 2.
 *
 * Luckily I had a great I idea and remembered a bit of math from hashing that
 * the modulus operator could be used. I just needed a bigger pool of numbers
 * than 1-5 with uniform probability and then it hit me to use the tens place
 * and the ones place. that means I will get 11-15, 21-25...51-55. The test
 * proves it to be pretty stnadard
 *
 * I am just looking up other solutions now and it seems mine is a bit novel
 */
