class Father1:

    def money(self):
        print("Father1 money")

class Father2:
    def money(self):
        print("Father2 money")

class Child(Father1, Father2):

    def give_money(self):
        print("Son")
        self.money()


obj=Child()
obj.give_money()