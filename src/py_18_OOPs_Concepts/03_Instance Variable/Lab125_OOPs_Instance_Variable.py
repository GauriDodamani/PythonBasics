a = 10 # variable can be used everywhere in the program
class Person:
    b = 15 # Instance variable used only within the class

    def print_info(self):
        c = 20 #     Local variable used only within the method/ function
        print(c)
        print(self.b)
        print(a)


object_ref = Person()
#print(b)       # not accessable as it is outside the class
#print(c)