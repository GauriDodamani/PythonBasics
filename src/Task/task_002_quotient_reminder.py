# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

# // -> this sign is used for quotient
# %  -> this sign is used as reminder

'''
 n1=input("enter 1st no: ")
TypeError: unsupported operand type(s) for //: 'str' and 'str'
Convert the str into int
'''

n1=int(input("enter 1st no: "))   #convert input() str to int using int()
n2=int(input("enter 2nd no: "))
q=n1//n2
r=n1%n2
print("The quotient is:",q)
print("The remainder is:",r)

