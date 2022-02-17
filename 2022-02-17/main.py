# Shaun Leung
# Feb 17, 2022
"""
This one is interesting in that they added the wrinkle of having 
a time stamp on keys. I dont think it is that tough all you have
to do is make a dictionary (I suppose we could just use a normal
array) and have the value be an array with the time being the index
then when writing the get function you just have to check the index
and if it isnt there work backwards until you get a recorded value.
"""

class timeDict:
    def __init__(self) -> None:
        self.dictionary = {}

    def set(self, key,value, time):
        if time < 0:
            print("Cannot have negative time")
            return

        if key not in self.dictionary:
            self.dictionary[key] = {time:value}

        else:
            self.dictionary[key][time] = value

    def backcheck(self,key, time):
        if time <0:
            return None
        
        if time not in self.dictionary[key]: # not to worry since it is a dict it is constant
            return self.backcheck(key,time-1)
        
        return self.dictionary[key][time]

    def get(self,key,time):
        if key not in self.dictionary:
            print("No key exists")
            return

        return self.backcheck(key, time)
            

# Testing
print("Fist Test")
db = timeDict()
db.set(1,1,0)
print("set: key: 1 value: 1 time: 0")
db.set(1,2,2)
print("set: key: 1 value: 2 time: 2")
print("get: key: 1 value:",db.get(1,1),"time: 1")
print("get: key: 1 value:",db.get(1,3),"time: 3")

print("Second Test")
db = timeDict()
db.set(1,1,5)
print("set: key: 1 value: 1 time: 5")
print("get: key: 1 value:",db.get(1,0),"time: 0")
print("get: key: 1 value:",db.get(1,10),"time: 10")

print("Third Test")
db = timeDict()
db.set(1,1,0)
print("set: key: 1 value: 1 time: 0")
db.set(1,2,0)
print("set: key: 1 value: 2 time: 0")
print("get: key: 1 value:",db.get(1,10),"time: 0")