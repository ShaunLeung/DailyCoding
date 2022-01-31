//Shaun Leung
// Jan 24, 2022

/***
 * This one actually should not be too bad. There was a similar question last
 * month but it was reversed, they gave you rand5 and you needed to make rand7.
 *
 * The first stab might be something like re-roll if the rand # is not in range
 * but that has a really niched edge case of going on indefinitly.
 *
 * A better solution would be to use hashing. In this instance I will just get
 * the sum of rand7 10 times and return mod 5
 */

const rand7 = () => {
  return Math.floor(Math.random() * 7 + 1)
}

const rand5 = () => {
  var sum = 0
  for (var i = 0; i < 10; i++) sum += rand7()
  return (sum % 5) + 1
}

array = [0, 0, 0, 0, 0]

for (var i = 0; i < 1000; i++) {
  array[rand5() - 1]++
}

console.log(array)
