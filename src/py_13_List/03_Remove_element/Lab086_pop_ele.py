#pop()/ pop(1/2/3/..../n)-->index

my_list=['apple','banana','orange','strawberry','kiwi']
list1=my_list.pop()     # removes last element as no specified index
print(list1)            # kiwi
print(my_list)          # ['apple', 'banana', 'orange', 'strawberry']


list2=my_list.pop(0)    # element removed of index 0  -> apple
print(list2)            # apple
print(my_list)          # ['banana', 'orange', 'strawberry']

"""
Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.
"""