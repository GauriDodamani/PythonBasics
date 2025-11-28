# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .


n1=int(input("Enter 1st no:"))
n2=int(input("Enter 2nd no:"))
n3=int(input("Enter 3rd no:"))

if n1>=n2 and n1>=n3:
    print("n1 is maximum")
elif n2>=n1 and n2>=n3:
    print("n2 is maximum")
else:
    print("n3 is maximum")