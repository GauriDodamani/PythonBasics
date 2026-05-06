class MathOperator:

    def div (self,a,b):   #self is required for
        return a/b

    @staticmethod
    def div1(c,d):   #if annotation is given then self is not required 
        return c/d

p=MathOperator()

print("Self arg is passed & is non static method as no annotation is used : " , p.div(15,3))


print("This is static method as @nnotation is used : " , MathOperator.div1(20,4))