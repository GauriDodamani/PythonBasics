class Car:


    def __init__(self,name_car,make_car,model_car):
        self.name = name_car
        self.make = make_car
        self.model = model_car


    def start_engine(self):
        print("Enter the name of car", self.name)
        print("Enter the making of car", self.make)
        print("Enter the model of car", self.model)


amaze=Car("Amaze","i vtech","2022")
amaze.start_engine()


lambo= Car("Lambo", "v6","2024")
lambo.start_engine()

