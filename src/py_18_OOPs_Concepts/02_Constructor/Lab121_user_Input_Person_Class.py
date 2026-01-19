class Person:

    #User input in DC
    def __init__(self):
        self.name = input("Enter your name:\n")
        self.age = input("Enter your age:\n")
        self.phone = input("Enter your phone:\n")
        self.address = input("Enter your address:\n")
        self.occupation = input("Enter your occupation:\n")

    def entered_details(self):
        print("Name is: " ,self.name," Age is: ",self.age," Phone is:",self.phone," Address is: ",self.address," Occupation is: ",self.occupation)


gauri = Person()
gauri.entered_details()
