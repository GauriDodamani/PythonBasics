class Home:

    def __init__(self):
        self.public_var = "Father"
        self.__private_var = "Baby"

    def mom(self):    #public function
        print(self.__private_var)
        self.__wife()           #can be accessed only within the class

    def __wife(self):
        print("I am private function cannot come outside the class and can be accessed only by inside the class")

access = Home()
access.mom()

# access.__private_var            #private variable
# access.__wife()                 #private function/ method
