#4 Copy() : copy the list

my_list=['apple','banana','orange','strawberry','kiwi']
print(my_list)

copied_list=my_list.copy()
print(copied_list)

copied_list.remove('banana')
print(copied_list)
'''
['apple', 'banana', 'orange', 'strawberry', 'kiwi']
['apple', 'banana', 'orange', 'strawberry', 'kiwi']
['apple', 'orange', 'strawberry', 'kiwi']

'''