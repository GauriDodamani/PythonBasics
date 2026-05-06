#Static Method: a method i.e @staticmethod belongs to a class, no need to create instance of the class
# can be called direct by Classname.method()

class Utility:

    @staticmethod           # annotation of staticmethod
    def greet(name):
        print("Hi", name)


    def greet1(self, name):
        self.name = name
        print("Hello,", name)


Utility.greet("Gauri")  # to access staticmethod function need to call (classname.method())
t=Utility()
t.greet1("Gauri Dodamani")
