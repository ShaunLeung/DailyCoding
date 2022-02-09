# Shaun Leung
# Feb 8, 2022

"""
I havve no idea why this one is labled as medium when it seems pretty easy,
maybe a little mathy.

just basically a loopp that counts up to the numerator incrementing by the 
demoninator, assuming it isnt 0.
"""

def division(den,num):
    if num == 0:
        return "error"
    out = 0
    for _ in range(0,den,num):
        out+=1
    return out


print(division(10,2))
print(division(10,0))
print(division(2,10))