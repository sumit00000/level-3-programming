
#function
#function - methods

def greetings( name ):
    "function docString"
    print("Hello,", name)
    return
greetings("3")


#user_creation function

def user_creation(name, email, phone):
    print("Name is:", name)
    print("email is:", email)
    print("phone is:", phone)

user_creation("sumit", "sumit@example.com", 98000000)

#let see that we don't want to print  phone then we have to finalize "phone=0" otherwise we got an error