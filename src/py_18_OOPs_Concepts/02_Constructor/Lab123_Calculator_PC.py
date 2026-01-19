class Calculator:
    a=None
    b=None

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

objref_c = Calculator(13,5)
print("Sum is : ",objref_c.sum())
print("Sub is : ",objref_c.sub())
print("Mul is : ",objref_c.mul())
print("Div is : ",objref_c.div())

