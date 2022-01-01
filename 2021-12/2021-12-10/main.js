/**
 * Shaun Leung 
 * Dec 10, 2021 
 * 
 * I think I had a dynamic programing question in school that we pretty similar 
 * to this question but it didn't give you the line limit which I think makes 
 * this question much easier.
 * 
 * spitballing soluitions is that we make a new array an insert words into it
 * until we hit the line limit. this way we know that all even number indexes, 0
 * included, are words and all odd indexes are spaces that may or may not need
 * to be padded. 
 * 
 * Things to keep track of are line length and how spaces will impact them. 
 * After the new aray is done it can just be joined together 
 */

const justified = (array, k) => {
    const outArray = []
    var i = 0
    // walk through the array of words. 
    while (i < array.length) {
        var len = 0
        var line = []
        // Cram words into the line
        while (len + array[i].length <= k - 1) {
            //add word and where the space will be
            line.push(array[i])
            line.push(' ')

            //update the length +1 is for the space we will put in
            len += array[i].length + 1

            //onto the next word. 
            i++

            //escape here so we dont error out on forward check on the next loop
            if (i >= array.length)
                break
        }

        if (line.length > 2) {
            len--
            line.pop()
        }

        //fill up the line by adding spaces
        for (var j = 1; len < k; j += 2) {
            //handle edge case if there is only 1 word on the line
            if (line.length == 2)
                while (len <= k) {
                    line[j] += ' '
                    len++
                }

            //loop back to the first space skipping the last space
            if (j >= line.length - 1)
                j = 1

            //add a space
            line[j] += ' '
            len++
        }
        // joing the line together
        outArray.push(line.join(''))

    }
    return outArray
}

const array = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
const newArray = justified(array, 16)
console.log(newArray)
//just a sanity check b/c I hate counting characters manually
for (var i = 0; i < newArray.length; i++) {
    console.log(newArray[i].length)
}
