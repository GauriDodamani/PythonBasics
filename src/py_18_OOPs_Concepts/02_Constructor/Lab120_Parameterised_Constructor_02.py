class Dog():

    #Attributes-> Instance variable / data variables
    name=None
    age=None
    breed=None
    color=None
    isVaccinated=None


    #Parameterised Constructor as 2 more variables / arguments are passed -> name,breed

    def __init__(self,nameGiven,breedGiven):
        print("This is Parameterised Constructor")
        self.name=nameGiven
        self.breed=breedGiven

    #Behavior

    def bark(self):
        print("Barking")

    def talk(self):
        pass

    def sleep(self):
        print("Sleep " + self.name)


coco=Dog("Coco","Beagle")
suzi=Dog("Suzi","Desi")

#objectref calls the function(method)
coco.sleep()
suzi.bark()