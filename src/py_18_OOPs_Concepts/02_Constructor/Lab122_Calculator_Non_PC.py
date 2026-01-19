class Calculator:
    a=None
    b=None

    # def __init__(self): # overrides the constructor
    #     print("DC_2")

    # def __init__(selfself,a,b): #TypeError: Calculator.__init__() missing 2 required positional arguments: 'a' and 'b'
    #     print("PC")

    def __init__(self):
        print("Default Constructor")

    def sum(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        return a / b

a= float(input("Enter a number : "))
b= float(input("Enter a number : "))

c_objref = Calculator()

sum = c_objref.sum(a,b)
sub = c_objref.sub(a,b)
mul = c_objref.mul(a,b)
div = c_objref.div(a,b)

print("Sum is: ",sum," Sub is: ",sub," Mul is: ",mul," Div is: ",div)