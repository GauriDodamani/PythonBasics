
try:
    a = int(input("Enter num1 : "))
    b = int(input("Enter num2 : "))
    c = a/b
    print(c)

except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Division by Zero")

except TypeError:
    print("Type Error")

except NameError:
    print("Name Error")

finally:
    print("Will always executed ")








