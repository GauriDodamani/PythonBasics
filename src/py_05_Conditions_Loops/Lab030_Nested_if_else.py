# Find the positive number is even or odd
#i/p-> int
#o/p-> str
#odd even logic= num%2==0 -> even else odd
#-v num -> invalid

n=int(input("Enter no:"))

if n>=0:
    if n%2==0:
        print("No is Even")
    else:
        print("No is Odd")
else:
    print("No is invalid/ negative no")



#one-liner ternary operator
n=int(input("Enter no:"))
if n>=0:
    print("No is Even" if n%2==0 else "No is Odd")
else:
    print("No is Invalid")