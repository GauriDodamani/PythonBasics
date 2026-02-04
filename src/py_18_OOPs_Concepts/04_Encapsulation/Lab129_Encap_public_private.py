class Home:


    def __init__(self):
        self.public_variable = "Father is a public variable"
        #self._protected_variable = "Mother is a protected variable" -- protected variable should be avoided in real project
        self.__private_variable = "Child is a private variable"


    def parents(self):
        #print(self.__private_variable)   # private variable are accessed within the class
        self.__private_variable = "Baby"    #change value to Baby (totally secured by parents method)

    def get_private_variable(self):
        return self.__private_variable      #return value


obj_ref= Home()
print(obj_ref.public_variable)   # public can be accessed outside/ anywhere in the class
#print(obj_ref._protected_variable)
#print(obj_ref.__private_variable)   #AttributeError: 'Home' object has no attribute '__private_variable'

obj_ref.parents()
print(obj_ref.get_private_variable())
