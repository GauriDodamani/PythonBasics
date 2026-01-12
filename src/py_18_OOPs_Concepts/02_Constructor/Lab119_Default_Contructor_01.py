print("Outside the class-1")

class MobilePhone:
    model = None

    def __init__(self):
        print("Default Constuctor")   #calls automatically

    def talk(self):
        print("Hi, Talking")



iPhone=MobilePhone()
iPhone.talk()
print("Outside the class-2")
