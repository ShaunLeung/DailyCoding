# Shaun Leung
# Feb 2, 2022

"""
This one is pretty interesing so I will walk through my thought process.
At first this seemed pretty close to those rand5/rand7 questions but I think
what they are looking for here is something close to buffering. Since the 
function that they give you is a read function that will return 0-7 characters
from the file and remember its place in the file the readN function should do 
likewise. 

The tricky part here is what to do with the remainder if N is not a factor of 7.
I am not a huge fan of saving it in some global variable so I think the best 
solution would be to back track on the file by the remainder of N/7. 

Since I am not very familiar with file operations in Python I did some research
and it looks like the seek function is what I am looking for since it will more
the pointer in the file. I will try to stay true to the spirit of the question 
and not do something cheap like just use the normal read function. 
"""


class File:
    def __init__(self, file) -> None:
        self.file = open(file, 'rb')

    def read7(self):
        return self.file.read(7).decode('UTF-8')

    def readN(self, n):
        reads = n // 7
        out = ""

        # read the file. we will always over read
        out += self.read7()
        for _ in range(reads):
            out += self.read7()

        # trim the excess if need be and go back in the file
        back = abs(len(out) - n)
        self.file.seek(-back, 1)

        if n < len(out):
            out = out[:n]

        return out


# testing
file1 = File('./2022-02-02/test.txt')
print(file1.read7())
print(file1.readN(7))
file1.file.close()

# swap
file2 = File('./2022-02-02/test.txt')
print(file2.readN(7))
print(file2.read7())
file2.file.close()

print("------------------------")
# when n < 7
file1 = File('./2022-02-02/test.txt')
print(file1.read7())
print(file1.readN(3))
file1.file.close()

# swap
file2 = File('./2022-02-02/test.txt')
print(file2.readN(3))
print(file2.read7())
file2.file.close()


"""
Not too bad had to fiddle around with seek and then the read functions a bit 
but it hoenstly wasen't too bad. 
"""
