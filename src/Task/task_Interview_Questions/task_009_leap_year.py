# Checking for a Leap Year , 2024 → Yes
# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.
# The year is multiple of 400.
# The year is a multiple of 4 and not a multiple of 100.


def leap_year(year):
    if (year%4==0 and year!=100) or (year%400==0):
        print(f"{year} is a leap year")
        #return True

    else:
        print(f"{year} is a not a leap year")
        #return False


y=int(input("Enter a year :"))
leap_year(y)



# result=leap_year(y)                      use this code to return true / false value
# print(f"It is {result}")