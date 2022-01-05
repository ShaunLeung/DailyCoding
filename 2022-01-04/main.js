// Shaun Leung
//Jan 04, 2022

/**
 * This one is pretty fun since there are only reall 4 things you can do.
 * Stack one pop
 * Stack one push
 * stack two pop
 * stack two push
 *
 * Also since there are no time complexity requirements we can do as many of
 * the above operations as we want.
 *
 * The plan is for a enqueue we just push onto the first stack. For Dequeue
 * things are a little more dificult since we are going to pop off every item
 * from stack one and push it onto stack 2, then we pop and return the first
 * item from stack two and then pop every remaining item from stack 2 and push
 * it back onto stack one
 */

class StackQueue {
  constructor () {
    this.stackOne = []
    this.stackTwo = []
    this.size = 0
  }
  /**
   * Adds and item to the Queue and increases the size
   * @param {*} item
   */
  enqueue (item) {
    this.stackOne.push(item)
    this.size++
  }
  /**
   * Offloads stackOne to stackTwo to so the oldest item can be accessed
   * and then rebuilds stackOne as the base state.
   * @returns {*} item
   */
  dequeue () {
    //guard against dequeue on an empty queue
    if (this.size === 0) throw 'Queue is empty'

    for (var i = 0; i < this.size; i++) {
      this.stackTwo.push(this.stackOne.pop())
    }
    var item = this.stackTwo.pop()
    this.size--
    for (var i = 0; i < this.size; i++) {
      this.stackOne.push(this.stackTwo.pop())
    }
    return item
  }
}

//Testing

queue = new StackQueue()

console.log('Enqueue: 1')
queue.enqueue(1)
console.log('Dequeue: ' + queue.dequeue())

console.log('Enqueue: 1')
queue.enqueue(1)
console.log('Enqueue: 2')
queue.enqueue(2)
console.log('Enqueue: 3')
queue.enqueue(3)
console.log('Enqueue: 4')
queue.enqueue(4)
console.log('Enqueue: 5')
queue.enqueue(5)

console.log('Dequeue: ' + queue.dequeue())
console.log('Dequeue: ' + queue.dequeue())
console.log('Dequeue: ' + queue.dequeue())
console.log('Dequeue: ' + queue.dequeue())
console.log('Dequeue: ' + queue.dequeue())

/**
 * This one was actually pretty easy. One design decision I made was to record
 * the size of the queue on my own and have it updated on each enqueue and
 * dequeue. I wanted the stacks to be pretty atomic and didn't want to rely to
 * heavily on array functions to get things done.
 */
