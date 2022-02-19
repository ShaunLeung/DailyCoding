# Shaun Leung
# Feb 19, 2022

"""
This one made me think for a second. At first I thought it was a dynamic
programing question but there were too many things to check. One of my first
ideas that I mistakenly dismissed out of hand was to use a dictionary since
a hash map would allow us to do things much faster. 

The other thing that tripped me up for a while with this challenge was the
time complexity requirement. For some reason hearing O(n) makes me thing that
there is no way that you can have nested loops. The thing I realized was that 
you can have nested loops as long as you arent looking at an element more than 
once.

So here is the plan, one pass to put all the elements in a dictionary with the 
key and value being the same (this means that we can effectively filter out any
duplicate numbers as well).

Next step is to do another pass of that dictionary to check for starting positions.
This is where the dictionary reall shines because we are able to check if a key exists
in constant time with the expression get(key), the trick is we want to check each 
entry for an entry that is immeduatly before it. This means checking for key-1.

Once we have our list of starting positions you can just count how many consecutively
come after. Now while this may be in a nexted loop each element in the list will only
be hit once.
"""

def consecutive(array):
    """
    Finds the number of consecutive elements in an  unsorted array of ints.

    @Param{[int]}   The unsorted array of ints to be looked at
    @Return{int}    The number of the longest set of consecutive ints
    """

    # load the dictionary
    dic = {}
    for num in array:
        dic[num] = num

    # check for starts
    starts = []
    for num in dic:
        if not dic.get(num-1):
            starts.append(num)
    
    # count which start is longer
    max = 0
    for num in starts:
        cur = 1
        i = 1

        while dic.get(num+i):
            cur +=1
            i+=1

        if cur > max:
            max = cur

    
    return max
            

array = [100, 4, 200, 1, 3, 2]
print(array)
print("Longest consecutive:", consecutive(array))

array = [2, 4, 2, 1, 3, 2]
print(array)
print("Longest consecutive:", consecutive(array))