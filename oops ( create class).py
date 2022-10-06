

#oops concept
#How to create a class

class Phone:
    "A simple class for test"
    phone_version = "S10"
    brand_name = "Samsung"
    user_name = ""

    #constructor
    def __init__(self, user_name):
        self.user_name = user_name

    def BootLogo(self):
        print("SAMSUNG", self.phone_version)

sumit = Phone("sumit phone")

sumit.BootLogo()
