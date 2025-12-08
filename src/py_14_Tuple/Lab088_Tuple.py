#Tuple --> Unchangeable with ordered collection of items.
#tuple are in round brackets -->()


my_tuple=(1,2,3,4,5)
print(my_tuple)
#my_tuple[0]=10    #TypeError: 'tuple' object does not support item assignment


#Mixed data type:
mixed_tuple=(12,"kiwi",9,"apple",3.14,True)
print(mixed_tuple) #(12, 'kiwi', 9, 'apple', 3.14, True)
print(type(mixed_tuple))  #<class 'tuple'>


#tuple with single element
single_tuple=(6,)   #comma should be given for single tuple
print(single_tuple) #(6,)
