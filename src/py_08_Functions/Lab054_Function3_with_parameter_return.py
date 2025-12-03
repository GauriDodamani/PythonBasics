#Function 3 -> with Parameter & with return value

def sum_of_num(a,b):
    return a+b
#    return "gauri"          # Data type doesn't matter parameter

result=sum_of_num(4,8)   #to get a return value, store the value in a variable name eg: result
print("The addition of the num is : ",result)


def sub_of_num(a,b):
    return a-b

result=sub_of_num(4,8)
print("The subtraction of the num is : ",result)



#when added num in str '' ,need to convert in integer using int()
result= sub_of_num(int('123'),int('120'))
print(f"The subtraction of the num is : {result}")


#when added num in str ''
result= sub_of_num('123','120')
print(f"The subtraction of the num is : {result}")
'''
    return a-b
           ~^~
TypeError: unsupported operand type(s) for -: 'str' and 'str'
'''