# Shaun Leung
# Nov 18, 2021 yes I know I am a day behind

# given code
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# a and b have been localized to the cons function to the pair function has
# access to them 

# input is a function
def car(pair):
    def f(a,b):
        return (a,b)
    return pair(f)[0]

def cdr(pair):
    def f(a,b):
        return (a,b)
    return pair(f)[1]



# Challenge tests
print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

# take away
# you have to define f as well and include it in your definitions of car & cdr