// Shaun Leung
// Feb 16, 2022

/**
 * Alright after yesterday's question this one is pretty easy. 
 * All I have to figure out is how many permutations I need to make.
 * 
 * Luckily there is a formula for that. n!/(n-r)! just need to write 
 * small facotrial helpwer problem which is pretty easy.
 */

const fact = n =>{
    if (n===0)
        return 1
    return n*fact(n-1)
}

//Borrowed code
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

const permutations = array => {
    perm = [[...array]]
    for (var i =1; i<fact(array.length);i++)
        perm.push([...nextLexico(array)])
    return perm
}

array = [1,2,3]
console.log(permutations(array))

/**
 * Today I leaned about the spread operator (...) to make a quick shallow copy
 */