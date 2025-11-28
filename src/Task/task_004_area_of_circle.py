# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14) / 3.14159265359

#Impotant steps:
#step1: always ask interviewer what data type for i/p & o/p to take
#step2: build logic in rough format
#step3: use logic building formula
#area=pi*r**2   convert into different ways according to function

#i/p-> float
#o/p-> string formatted
#pi=3.14
#r-> float->input
#can use pow function for radius
pi=3.14159265359
radius=float(input("Enter the radius : "))
print(radius)
area= pi*(radius**2)
#area= pi*(pow(radius,2))   # power function used pow(r,2)
#print area using string format {}

#print("The area of the circle is",area)
print(f"The area of the circle is : {area:.2f}")   # string format f{}















'''
#take radius of the circle -3
#pi = 3.14
#area=formula

pi= 3.14
radius=float(input(" Enter the radius of the circle : "))
area = pi*radius**2
print("The area of the circle is :", area)

'''