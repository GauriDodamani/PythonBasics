# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.
# clear(): removes all items.


#remove()   : removes by value
my_list=['apple','banana','orange','strawberry','kiwi']

my_list.remove('banana')  #value passed
print("Removed value : ",my_list)

#Remove by value :  ['apple', 'orange', 'kiwi']


"""
Remove first occurrence of value.

Raises ValueError if the value is not present.
"""