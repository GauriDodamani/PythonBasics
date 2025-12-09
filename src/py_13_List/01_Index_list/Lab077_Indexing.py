# index() -> starts with 0

number=[10,20,30,40,50,100]

#index()
print(number.index(100))   # gives index value   ---> o/p: 5

"""
Return first index of value.

Raises ValueError if the value is not present.
"""

#slicing
print(number[1:4])  # element from index 1 to 3    -> o/p:  [20, 30, 40]


#last element
print(number[-1])   #access last element of list   -> o/p: 100



#true or false
print("apple" in number)  #False
print(20 in number)   #True

my_list=['apple','banana','orange','strawberry','kiwi']
print(f"Element of index 0 is : {my_list[0]}")
print("Element of index 1 is :",my_list[1])
print("Element of index 2 is :",my_list[2])
print("Element of index 3 is :",my_list[3])

'''
Element of index 0 is : apple
Element of index 1 is : banana
Element of index 2 is : orange
Element of index 3 is : strawberry

'''