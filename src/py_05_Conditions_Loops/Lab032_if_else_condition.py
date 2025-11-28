# Problem to find the max between two.

# Logic Building Formula

# i/p -> two integers
# o/ p ->  int 1, which ever is grater max number it will return.
# 31.4 or 45.34 - float


n1=float(input("Enter the first no:"))
n2=float(input("Enter the second no:"))

# if n1>0 and n2>0:
#     print("Number should be positive")      # ask interviewer about the +ve & -ve senario

if n1>=n2:        #both no are equal than also if condition o/p will print
    print("first no is maximum")
else:
    print("second no is maximum")