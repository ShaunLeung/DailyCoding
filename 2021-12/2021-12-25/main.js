/**
 * Shaun Leung
 * Dec 26, 2021
 *
 * Well this problem is deceptively tricky. I thought it would be really
 * Straight forward when I first saw it but the constraint of having all
 * the opperations be in constant time reall makes it rough.
 *
 * It honestly never occured to me to push on a number that wasent the one
 * passed since you can only get the number out of the stack if you pop it.
 *
 * the solution requires you to push a number that is larger than then recorded
 * max and when you come across the case when you pop off a number that is
 * larger than the recorded max you simply return then recorded max, remove the
 * latest, and update what the new max should be.
 */

class MaxStack {
  constructor () {
    this.max = null
    this.stack = []
  }

  pop () {
    //handle and invalid operation
    if (this.stack.length == 0) {
      console.log('Stack is empty')
      return null
    }
    var num = this.stack.pop() //kinda cheating
    if (num > this.max) {
      var oldMax = this.max
      this.max = num / 2 - this.max
      num = oldMax
    }
    // the list is now empty
    if (this.stack.length == 0) this.max = null

    //return the value
    return num
  }
  push (num) {
    if (null == this.max) {
      this.max = num
    }

    if (num > this.max) {
      var oldMax = this.max
      this.max = num
      num = (num + oldMax) * 2
    }
    this.stack.push(num) //kinda cheating but not really
  }
  getMax () {
    return this.max
  }
}

var stack = new MaxStack()

console.log('Stack: ' + stack.stack)
console.log()

console.log('pushing 1')
stack.push(1)
console.log('Stack: ' + stack.stack)
console.log('max ' + stack.max)
console.log()

console.log('pushing 2')
stack.push(2)
console.log('Stack: ' + stack.stack)
console.log('max ' + stack.max)
console.log()

console.log('popping ' + stack.pop())
console.log('Stack: ' + stack.stack)
console.log('max ' + stack.max)
console.log()

console.log('pushing 100')
stack.push(100)
console.log('Stack: ' + stack.stack)
console.log('max ' + stack.max)
console.log()

console.log('pushing 4')
stack.push(4)
console.log('Stack: ' + stack.stack)
console.log('max ' + stack.max)
console.log()

console.log('popping ' + stack.pop())
console.log('Stack: ' + stack.stack)
console.log('max ' + stack.max)
console.log()

console.log('popping ' + stack.pop())
console.log('Stack: ' + stack.stack)
console.log('max ' + stack.max)
console.log()

/*
 * Looks good! and not a loop to be seen!
 */
