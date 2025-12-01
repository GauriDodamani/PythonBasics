#Take a input from user
#If age is less than 18 not allowed to vote
#create the given code in onr-liner Ternary

# age=int(input("Enter the age : "))
# if age >= 18 :
#     print("You are allowed to vote")
# else:
#     print("You are not allowed to vote")


age=int(input("Enter the age : "))  # int() need to add for integer value
print("You are allowed to vote" if age>=18 else "You are not allowed to vote")