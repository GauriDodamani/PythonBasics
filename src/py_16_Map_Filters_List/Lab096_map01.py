#map(): Apllies a function to each item in a list and return a map object
# map needs to convert into List to get o/p
#  map(function, iterable)


numbers=[1,2,3,4,5]

#define function
def sq(x):
    return x**2

#calling function
sq_all_num= map(sq, numbers)
print(sq_all_num)

#o/p: <map object at 0x00000172E9C20490>

#Converted to list
sq_all_num= list(map(sq, numbers))
print(sq_all_num)

#o/p: [1, 4, 9, 16, 25]