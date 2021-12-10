/**
 * Shaun Leung
 * Dec 9, 2021
 * 
 * Ahhh, the classic bracket matching problem. Surpsingly I have never done this
 * one before.
 * 
 * first thoughts is you just make a stack and push on the compliment if it is
 * open bracket and pop and compare if it is a close. if you get a miss match
 * you can return false early
 */

const balancedBrackets = string => {
    const open = ['(', '{', '[']
    const closed = [')', '}', ']']
    var stack = []
    for (var i = 0; i < string.length; i++) {
        //build the stack
        if (open.includes(string[i]))
            //push the compliment
            switch (string[i]) {
                case '(':
                    stack.push(')')
                    break
                case '{':
                    stack.push('}')
                    break
                case '[':
                    stack.push(']')
                    break
            }
        else {
            item = stack.pop()
            if (item != string[i])
                return false
        }

    }

    //still something on the stack
    if (stack.length != 0)
        return false

    return true
}

//testing
var string = "([])[]({})"
console.log(string)
console.log(balancedBrackets(string))
console.log('************************')

string = "([)]"
console.log(string)
console.log(balancedBrackets(string))
console.log('************************')

string = "((()"
console.log(string)
console.log(balancedBrackets(string))
console.log('************************')