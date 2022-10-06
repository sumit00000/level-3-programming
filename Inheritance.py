

#oops concept
#Inheritance from Nokia to Iphone

class Nokia:
    def __int__(self):
        print("I am Nokia")

    def makeScreen(self):
        print("I make screens")

class Iphone(Nokia):
    def __int__(self):
        print("I am Iphone")

    def a3chips(self):
        print("I make A3 bionic chips")

user = Iphone()

user.a3chips()
user.makeScreen()

