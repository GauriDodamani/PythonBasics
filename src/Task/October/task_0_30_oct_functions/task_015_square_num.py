# Q - Create a function which will take a positive number from the user
# and perform square of the number?
# i/o = 3
# o/p = 9
#Function-> With parameter & With return value

#My logic:

def num(a,b):
    if a>0:
        return a ** b
    else:
        return None

result=num(a=int(input("Enter a positive number : ")),b=0.5)
print(f"The square of positive number is : {result}")



#Another logic:

def square(a,b):
    if a>0:
        return a ** b
    else:
        return None

a=float(input("Enter a positive number :"))
result= square(a,b=0.5)

if result is not None:
    print(f"The square root of positive number is : {result}")
else:
    print("Entered number is Negative")