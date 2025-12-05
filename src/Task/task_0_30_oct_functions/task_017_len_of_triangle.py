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
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            if a==b==c:
                print("The length of the triangle is Equilateral")
            elif a==b or a==c or b==c:
                print("The length of the triangle is Isosceles")
            else:
                print("The length of the triangle is Non-Isosceles/Scalene")
        else:
            print("No a Triangle")
    else:
        print("No a Valid length")

side1=float(input("Enter the a side of the triangle : "))
side2=float(input("Enter the b side of the triangle : "))
side3=float(input("Enter the c side of the triangle : "))

len_of_triangle(side1,side2,side3)

