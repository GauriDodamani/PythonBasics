# keywords- if, elif, else
#if

age=23

if age > 18:
    print("Entered value is true and age is",age)

print("Entered value is false")


i = 10

# Checking if i is greater than 15
if i > 15:
    print("10 is less than 15")

print("I am Not in if")


#if-else

age=35
if age<20:
    print("Im looking for a job")
else:
    print("Im working")


gender="F"

if gender=="F":
    print("I am Female")
else:
    print("I am Male")


#if-elif-else

marks=16

if marks >=30 and marks <=50 :
    print("Your grade is C ")
elif marks >=51 and marks <=80 :
    print("Your grade is B")
elif marks >=81 and marks <=100:
    print("Your grade is A")
else:
    print("Your are failed")


#dynamically from the user
marks=int(input("Enter the marks:"))

if marks >=20 and marks <=50 :
    print("Your grade is C ")
elif marks >=51 and marks <=80 :
    print("Your grade is B")
elif marks >=81 and marks <=100:
    print("Your grade is A")
else:
    print("Your are failed")
