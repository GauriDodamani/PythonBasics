# Given a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Factorial (n!) for 0!=1
from math import factorial

# for n in range(1,5,1):
#     print("Factorial")

num=int(input("Enter a number :"))

factorial=1
#for i in range(i,
for i in range(1,num+1):    #num will be going from 1 to n-1 so -< n+1 added
    factorial = factorial * i  # this value will be stored in next factorial
    print("The factorial : ", factorial)



#while loop
num=int(input("Enter a number :"))
factorial=1
counter=1

while counter<=num:
    factorial = factorial * counter
    print("The factorial : ", factorial)
    counter = counter + 1