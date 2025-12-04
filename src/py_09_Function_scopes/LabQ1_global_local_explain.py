# Local Variable--->
# defined and accessible only within function.
# Created when the function is called
# destroyed when the function finishes execution.

# Global Variable --->
# defined outside of any function or class
# accessible from anywhere within the program, including inside functions.

count = 0   #golbal variable

def increment_count():
    #UnboundLocalError: local variable 'count' referenced before assignment
    #count = count + 1 # This line will cause an error as it considers a local variable with value

    global count       # So, global var is define inside the function
    count = count + 1   #updated golbal var
    print(count)

increment_count()
print(count)    #As


'''
1: Count=0   -> Global Variable
2: define function
3: count=count+1  -> it is considering a local variable and gets error so code never gets execute 
4: to get execute->  we need to define "global" inside the function
5: global count-------> golbal var 
6: count= count+1  -> count inside the function means the same count as outside and no local variable
7: 0+1=1   -> gets golbal updated value into the function
8: print(count)----------->is increased into the function , value updated
9: Updated value will be printed outside the function 
'''