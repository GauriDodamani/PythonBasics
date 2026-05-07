#Multiple Exception error



try:
    a = int(input("Enter num1 : "))
    b = int(input("Enter num2 : "))
    c = a/b
    print(c)

except (ValueError, NameError, ZeroDivisionError,TypeError):
    print("Error due to : ValueError, NameError, ZeroDivisionError,TypeError")







