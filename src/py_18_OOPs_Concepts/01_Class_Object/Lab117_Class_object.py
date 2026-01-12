class Person:
    #Attributes
    name=None
    id=0
    age=None
    gender=None
    phone_no=None
    address=None

    #Behavior
    #Method is within the class

    # self- it is the first argument in every method

    def talk(self):     # No Arg No Return
        print("I can talk")

    def walk(self, name):  # Arg with No Return
        print("I am a talk Method")
        print("Walk", name)

    def sleep(self, name):  # Arg with return
        print("I am a Sleep Method")
        return None

    def walk_return(self):  # No Arg with Return
        return "I am Walking"


#Function is outside the class
def outside_class():
    print("I am Function")



#create a object of a class
#objectRef = className() -> object
gauri = Person() #Person()  -> it is a object


# using objectRef can access the attribute & behavior

print("What is Gauri age: ",gauri.age)    # attribute
gauri.walk("Vinit")    # behavior




#2nd example
vinit= Person()
print("Vinit can I know your adds:",vinit.address)
vinit.talk()
vinit.walk("Vinit")
vinit.sleep("Vinit")
print(vinit.walk_return())



