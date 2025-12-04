count = 0       #Global var

def increment_count(current): #parameter will take 2 value
    current = current + 1                   #b=2+1
    print("Print the local var value : ",current)  # print 3
    return current*2   #to understand added *2     #return 3 and multiple by 2
#return that value to a1  ->3*2=6
#a1 = increment_count(count)
count = increment_count(2) #argument value pass 2
print("Print the golbal var value : ",count)     #priint 6


'''
1: a1=increment_count(2)   argument passed
2: increment_count(count) count is replace by 2 , so this 2 given value to parameter current
3: current =2
4: current=current+1----> current=2+1
5: print(current)---> 3
6: return current*2 ---> 3*2=6   new return value
7: store new return value into a1
8: print(count)--->8


Simple Understanding :

You are passing a value into a function
The function increases the value
It sends the new value back
You store that returned value back into count
'''