#one line code - recommened not to use
#
# square = {x ** 2 for x in range (5)}
# print(square)
# # {0, 1, 4, 9, 16}


squ = []
for x in range (5):
    squ.append(x ** 2)

result=set(squ)
print(result)
# {0, 1, 4, 9, 16}


# frozenset()-Immutable/ Unchangeable and removes duplicate element
# Can't be changed after creation

fset = frozenset([1,2,3,4,5,3,6,7,3,5,8])
print(fset)

#  frozenset({1, 2, 3, 4, 5, 6, 7, 8})