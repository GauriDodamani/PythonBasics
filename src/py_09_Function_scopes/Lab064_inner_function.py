def outer_function():
    var1=10

    def inner_function1():
        var2=9
        print("This is outer function value : ",var1)
        print("This is inner function value : ",var2)

    def inner_function2():
        var3=5
        print("This is inner function2 value : ",var3)
        #print("This is inner function1 value : ", var2)
     # unable to access other function value as it is local var

   # inner_function1()
    inner_function2()

outer_function()

#inner_function1   # can not be called outside the function
