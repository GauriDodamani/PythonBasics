# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# Step 1 - I/O and O/P
# I/O -  int
# O/P - int



n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
n3=int(input("Enter the third number : "))

def sum_of_three(num1=100,num2=200,num3=300):
    return num1+num2+num3

result_user=sum_of_three(num1=n1,num2=n2,num3=n3)


result0=sum_of_three()          #600
result1=sum_of_three(num1=10,num2=20,num3=30)   #60
result2=sum_of_three(20,80,20)  #120
result3=sum_of_three(num1=30)       #30+200+300=530
result4=sum_of_three(num2=40,num3=20) #100+40+20=160


print(result_user)
print(result0)
print(result1)
print(result2)
print(result3)
print(result4)



