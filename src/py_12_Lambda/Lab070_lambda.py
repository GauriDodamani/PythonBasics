#lambda: it used to simplify the one line code into lambda expression
#can't be used to print multiple value



def three_num(num):
    return num*3

result = three_num(2)
print(result)

#lambda function

result = lambda num : num * 3
print(result(6))