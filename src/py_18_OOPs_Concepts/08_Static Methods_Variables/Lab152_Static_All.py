class O:

    @staticmethod
    def div(a,b):
        return a/b


    @staticmethod
    def sum(a,b):
        return a+b


    @staticmethod
    def sub(a,b):
        return a-b


    @staticmethod
    def mul(a,b):
        return a*b

print("Divide:" ,O.div(9,3))
print("Multiple:" ,O.mul(9,3))
print("Addition:" ,O.sum(9,3))
print("Subtract:" ,O.sub(9,3))