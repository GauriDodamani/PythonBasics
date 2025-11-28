# Write a program to take a user age and
# let him know if he can go the club.
# 21

# We should consider edge cases such as:
# Negative ages or extremely high values -> program will break.
# Non-numeric input - ABC
# Age which is valid. > 130


#i/p - age-> int
#o/p - str
#strip()- it will remove spaces without editing original input


age=int(input("Enter the age :").strip())  # added 5 space before & after the sentence.

if age<0 and age>130:
    print("You are not valid")
else:
    if age>=21:
        print("You are allowed to enter the club")
    else:
        print("You are not allowed to enter the club")

#o/p: Enter the age :     12     After input given 5 spaces using strip() it removed that spaces and took only age
#You are not allowed to enter the club