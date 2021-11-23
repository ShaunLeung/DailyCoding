# Shaun Leung
# Nov 22, 2021

# This one seems pretty straight forward at first, but the main thing I want
# to address with this problem is that if you simply use the sleep function
# it is blocking and could cause issues if you wanted to to schedule more than
# one person at a time. A solution to this could be to make a new thread with a
# timer



import threading

def scheduler(f, n):
    t = threading.Timer(int(n/1000),f)
    t.start()
    
    return

def someFunction():
    print("second")
def someOtherFunction():
    print("first")

scheduler(someFunction,10000)
scheduler(someOtherFunction,9000)

# could have used JS here since it is inhernetly non-blocking but I wanted some 
# practice with threads and Python. 