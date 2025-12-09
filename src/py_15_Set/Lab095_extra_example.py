#one line code - recommened not to use
#
# square = {x ** 2 for x in range (5)}
# print(square)
# # {0, 1, 4, 9, 16}

squ = []
for x in range (5):
    squ= x ** 2
    result=set(squ)
    print(result)

'''
0
1
4
9
16

'''