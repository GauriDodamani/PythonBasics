# Exercise 1: Age and License Check
# Write a Python program that takes a user's age and a boolean has_license as input.
# If the user's age is 18 or above:
# If has_license is True, print "You can drive."
# Else, print "You need a license."
# Else (if the user's age is less than 18), print "You are too young to drive."


#logic build:

age=int(input("Enter your age:").strip())
has_license=bool(input("Do you have license :"))


if age>=18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

'''
o/p:
Enter your age:25
Do you have license :false
You can drive

'''


