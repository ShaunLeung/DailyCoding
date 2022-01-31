# Shaun Leung
# Jan 6, 2022

"""
This is kinda of an interesting questing because it wants you to emulate 
something that already exists. I think URL shorteners just keep a DB of 
URLS that have been shortened and do forward when that page is accessed. 

I am not sure if the shortened string is random though, it often looks like it.
I think you can do some interesting things with ascii where you can convert the input string to a # and then get out a shorter URL. The problem with this is that a collision might occur where 2 different strings are shortened to the same 6 characters. 

ascii 
Numbers:    48-57
Upper Case: 65-90
Lower Case: 97-122

An easy out will be to just pass back links that are already shorter than 6 chars
"""


class URL6:
    def __init__(self) -> None:
        self.dataBase = {}

    def toAN(self, num):
        """
        Since we only want 0-9, A-Z and a-z this function takes a number between
        0-62 and will spit out the corresponding char. 
        With:
        0-9 being 0-9
        10-35 being A-Z
        36-61 being a-z

        :Param num: number between 0-61 to be converted to alpha numeric
        :Return char: Converted char being returned. 
        """
        if num < 10:
            return chr(num+48)
        elif num < 36:
            return chr(num+55)
        else:
            return chr(num+61)

    def shorten(self, url, n=-1):
        """
        Shorten's a url and returns 6 alpha numeric characters which can be 
        added to another URL for forwarding. Saves the url and the shorter 
        version to a DB.

        Handles colisions by altering the hashing algorithm, gonna increase the
        amount subtracted by one. 

        :Param url: The URL to be shortened
        :Return string: The shortened URL
        """
        # if the url is < 7 chars it doesnt need to be shortened
        if len(url) < 7:
            self.dataBase[url] = url
            return url

        # for the recursive step, -1 is good since len cant be negative
        if n == -1:
            n = len(url)

        string = ""
        sum = 0
        for letter in url:
            sum += ord(letter)

        for _ in range(6):
            string += self.toAN(int(sum % 62))
            sum += n

        # if there is a collision
        if string in self.dataBase.keys():
            if url != self.dataBase[string]:
                string = self.shorten(url, n+1)

        self.dataBase[string] = url
        return string

    def restore(self, string):
        """
        very simple function. Just checks the DB if there is an entry and
        returns the value. If there isnt then it returns None. 

        :Param string: Shortened URL used as key in the DB
        :Return value: The URL in the DB
        """
        if string not in self.dataBase.keys():
            return None
        return self.dataBase[string]


# toAN test
alphNumeric = []
test = URL6()
for i in range(48, 58):
    alphNumeric.append(chr(i))
for i in range(65, 91):
    alphNumeric.append(chr(i))
for i in range(97, 123):
    alphNumeric.append(chr(i))

for i in range(62):
    if test.toAN(i % 62) not in alphNumeric:
        test.print(test.toAN(i % 62))


# Testing
string = 'www.shaunleung.com'
print(string)
shrt = test.shorten(string)
print(shrt)
print(test.restore(shrt), end='\n\n')

string = 'www.google.com'
print(string)
shrt = test.shorten(string)
print(shrt)
print(test.restore(shrt), end='\n\n')

string = 'www.shaunleung.com'
print(string)
shrt = test.shorten(string)
print(shrt)
print(test.restore(shrt), end='\n\n')

print("Trying to use string that isnt in DB")
shrt = "Dm8sW2"
print(shrt)
print(test.restore(shrt), end='\n\n')
