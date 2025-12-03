#Function 2 -> with Parameter & no return value

#Step 1-> Define/ Declare the function

def greet(name):       #name is the parameter with any data type
    print("Hi, ", name)

#Step 2-> Call the function

greet("Gauri")
greet(1234)         #function is reusable & no need to mention datatype of parameter int/str/any..




#FUnction with multiple parameter--->  First & last name

def greet_full_name(first_name,last_name):      #Can use multiple/ unlimited parameter
    print(f"Your full name is : {first_name} {last_name}")
#    print("Hi,", first_name , last_name)
#    print("Hi,", first_name + " " + last_name)

greet_full_name("Gauri", "Dodamani")




