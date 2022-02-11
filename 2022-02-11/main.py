# Shaun Leung
# Feb 11, 2022

"""
This one is interesting cause it is more of a syntax question which isnt the greatest.

Just gonna talk through my thought process here before I do any coding. 
First thing is to run the code given in the example which I believe should return an error
since it is just saving int 0-9 in the array and you cant do function calls on those. 

To fix it there are a few ways, assuming they want the numbers 0-9 printed out.
You could just recode it all and do it all in one loop but I dont think that is what
they are getting at.

You could also remove the brackets from the second loop but again I am not sure that is what
they are looking for with how the variables are named.

What I think they are looking for is to actually append function addresses to the array. 
"""



functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())

"""
The function will always print out 9 since that is the last value of i
Lambda functions are not made to store data but rather transform it. 

Right now all we have is a function that returns the variable i

what they might be looking for is adding a parameter onto the lambda function.
"""

functions = []
for i in range(10):
    functions.append(lambda i=i: i)

for i,f in enumerate(functions):
    print(f())


"""
I think this is what they were going for. but the question was vague enough that they could be looking for something else. 
"""