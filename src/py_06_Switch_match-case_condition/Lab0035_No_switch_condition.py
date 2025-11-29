# In Python there is no traditional switch condition used.
#In Python fron version -> 3.10+ match-case condition is used

day=input("Enter the day : ")

match day:
    case 1:
        print("Day is : Monday")
    case 2:
        print("Day is : Tuesday")
    case 3:
        print("Day is : Wednesday")
    case 4:
        print("Day is : Thursday")
    case 5:
        print("Day is : Friday")
    case 6:
        print("Day is : Saturday")
    case 7:
        print("Day is : Sunday")
    case _:
        print("Invalid")


#case _ : it always will be last case as it is default case
