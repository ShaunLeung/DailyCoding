//Shaun  Leung
//Feb 15, 2022

/**
 * This one took me a sec to figure out what they meany by lexicographically 
but I think I get it. The big hint for this one is that they want it done
in constant space.

So the idea of starting from the back came to me pretty quickly so you just
need to swap the back number with closest number that lesser. From there you
just need to go in reverse order from the lowest index swapping numbers so that
the lower numbers have lower indices. Not great for Time complexity but there were
no restrictions on that. 

The last thing is that if we get though the whole list of numbers and we never preform 
the first swap then we simply reverse the list. 
 */

const nextLexico = array =>{
    var size = array.length-1
    var cur = size -1
    //first swap
    for(var i= size;i>=1;i-- ){
        for(cur = size -1;cur>=0;cur--){
            if (array[cur] < array[i]){
                var temp = array[cur] //Swap
                array[cur] = array[i]
                array[i] = temp
                break
            }
        }
        if (cur != -1){
            break
        }
    }
    //at the end of lexicographical order start at the beginning
    if(cur == -1)
        return array.reverse()

    //get the rest in order
    cur++
    for (;cur<size;cur++){
        for(var i = cur + 1;i<=size;i++){
            if(array[i] < array[cur]){
                var temp = array[cur] //Swap
                array[cur] = array[i]
                array[i] = temp
            }
        }
    }
    return array
}

var array = [1,2,3]
console.log(array)
array = nextLexico(array)
console.log(array)
array = nextLexico(array)
console.log(array)
array = nextLexico(array)
console.log(array)
array = nextLexico(array)
console.log(array)
array = nextLexico(array)
console.log(array)
array = nextLexico(array)
console.log(array)

/**
 * Things I want to clean up:
 * better swap, can probabaly get this down to one line
 */