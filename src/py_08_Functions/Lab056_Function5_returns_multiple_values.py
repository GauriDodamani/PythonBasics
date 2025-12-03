#Function with Parameter Returns Multiple values

def math_of_num(a,b):
    return a+b, a-b, a*b, a/b, a//b, a%b, a**b    #returing multiple value

add,sub,mul,divs,quot,remainder,power = math_of_num(5,8)
print("The add of num is : ", add)
print("The sub of num is : ", sub)
print("The mul of num is : ", mul)
print("The divs of num is : ", divs)
print("The quot of num is : ", quot)
print("The reminder of num is : ", remainder)
print("The power of num is : ", power)


