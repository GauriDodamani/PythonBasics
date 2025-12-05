# def give_me_power(num):
#     return math.pow(num, 2)
#
# op=  give_me_power(10)
# print(op)
import math

user_input= int(input("Enter the number : "))
power = lambda power : math.pow(user_input,2)
print(power(user_input))



# can write whole pgrm into one line code

power = lambda : math.pow(int(input("Enter the number : ")),2)
print(power())