class Dog():
    #Attributes-> Instance variable / data variables
    name=None
    age=None
    breed=None
    color=None
    isVaccinated=None

    def __init__(self):
        print("I will be called")

    def bark(self):
        print("I will bark")

    def sleep(self):
        print("Sleep ")

    def talk(self):
        pass


cocoref = Dog()
suziref = Dog()


print(cocoref.name)
print(suziref.name)


#object.method
Dog().bark()
Dog().sleep()