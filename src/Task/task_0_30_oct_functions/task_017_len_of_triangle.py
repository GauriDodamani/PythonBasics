# Q - Create a function which will take the 3 values from the user,
# which are length of the triangle.
# side1, side2, side2
# i/p - int side1 == side2 =side3
# o/p = result in string - iso, eq, scalene

# Function-> With Parameter & no return value

#Types of triangle:
# Equilateral-All three sides are of equal length.
# Isosceles-Exactly two sides are of equal length.
# Scalene-All three sides are of different lengths.

def len_of_triangle(a,b,c):
    if a==b==c:
        print("The length of the triangle is Equilateral")
    elif a==b or a==c or b==c or c==a:
        print("The length of the triangle is Isosceles")
    else:
        print("The length of the triangle is Non-Isosceles/Scalene")

side1=int(input("Enter the a side of the triangle : "))
side2=int(input("Enter the b side of the triangle : "))
side3=int(input("Enter the c side of the triangle : "))

len_of_triangle(side1,side2,side3)

