# Write a program to calculate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")



user_input =int(input("Enter the number "))

check_even_odd = lambda num : "Even" if num%2==0 else "Odd"
print(check_even_odd(user_input))
