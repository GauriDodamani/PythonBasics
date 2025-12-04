golbal_var=12     #golbal variable

def my_function():
    local_var=4
    #print(local_var)        #local variable is executed/ called with in the function
    print(golbal_var)#----> golbal can access inner or outer function


# print(local_var)     # local variable can't be access outside the function
my_function()

