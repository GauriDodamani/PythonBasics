

try:
    a = int(input("Enter num1 : "))
    b = int(input("Enter num2 : "))
    c = a/b


except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Division by Zero")

except TypeError:
    print("Type Error")

else:
    print(c)

finally:
    print("Will always executed ")








