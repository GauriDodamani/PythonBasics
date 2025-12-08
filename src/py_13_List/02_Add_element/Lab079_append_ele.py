#List is mutable-> change
# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.


#1)append() - Adds 1 element at the end of the list.

my_list=['apple','banana','orange','strawberry','kiwi']

my_list.append('dragon')
print(my_list)
# ['apple', 'banana', 'orange', 'strawberry', 'kiwi', 'dragon']

my_list.append(10)
print(my_list)

# ['apple', 'banana', 'orange', 'strawberry', 'kiwi', 'dragon', 10]
