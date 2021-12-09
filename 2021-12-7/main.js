// Shaun Leung
// 2021-12-9

/** Regular expresiions, you either love them or hate them. Luckily this
 * challenge doesnt have you implement everything. Also it looks like we don't
 * have to do escape characters.
 * 
 * some edge cases to consider are if there are multiple wildcards in a row 
 */

/* Well I was making this much harder than I though and was doing partial 
* matching when I should have been doing complete matching. That means if a 
* letter doesnt line up I can immidialty return false...assuming the next char
* isnt an *
*/


const regexChecker = (string, pattern) => {
    ast = null
    dot = false
    j = 0; //index counter for the pattern
    //Walk through the string
    for (i = 0; i < string.length; i++) {
        if (j >= pattern.length && ast == null)
            return false

        // * handling
        if (pattern[j] == '*') {
            ast = pattern[j - 1]
            j++
            i--

            // need this here for the edge case of the previous char being a .
            if (ast = '.')
                dot = true

            continue
        }

        // . flagging
        if (pattern[j] == '.')
            dot = true

        if (string[i] == pattern[j] || string[i] == ast || dot) {
            //back to regular matching...get it?
            if (string[i] == pattern[j])
                ast = null
            //keep matching whatever
            if (ast == '.')
                continue

            //regular match
            dot = false
            j++
        }

        else {
            //last check to see if we have an * coming up and shouldnt return F
            if (j < pattern.length - 2)
                //nesting this b/c I dont trust lazy evaulation
                if (pattern[j + 1] == '*')
                    continue

            return false
        }
    }
    return true
}
// testing

string = 'ray'
pattern = 'ra.'
console.log(string)
console.log(pattern)
console.log(regexChecker(string, pattern))
console.log('*************************')

string = 'raymond'
pattern = 'ra.'
console.log(string)
console.log(pattern)
console.log(regexChecker(string, pattern))
console.log('*************************')

string = 'chat'
pattern = '.*at'
console.log(string)
console.log(pattern)
console.log(regexChecker(string, pattern))
console.log('*************************')

string = 'chats'
pattern = '.*at'
console.log(string)
console.log(pattern)
console.log(regexChecker(string, pattern))
console.log('*************************')
