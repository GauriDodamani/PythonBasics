# Given a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Factorial (n!) for 0!=1
from math import factorial

# for n in range(1,5,1):
#     print("Factorial")

num=int(input("Enter a number :"))
factorial=1

if num<0:
    print("Entered no is negative or undefined")

elif num==0:
    print("Factorial of 0 is:", factorial)
else:
    for i in range(1,num+1):    #num will be going from 1 to n-1 so -> n+1 added
        factorial = factorial * i  # this value will be stored in next factorial
        print(f"The factorial of {num} is: {factorial}")            #f-string



#while loop
print("\n")
print("While Loop")
num=int(input("Enter a number :"))
factorial=1
counter=1

if num<0:
    print("Entered no is negative or undefined")

elif num==0:
    print("Factorial of 0 is:", factorial)
else:
    while counter<=num:
        factorial = factorial * counter
        print("The factorial : ", factorial)
        counter = counter + 1