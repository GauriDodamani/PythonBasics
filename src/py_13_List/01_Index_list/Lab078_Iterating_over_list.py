my_list=['apple','banana','orange','strawberry','kiwi']
# 1) Iterating over list

for item in my_list:
    print(item)


'''
o/p:

Gauri
banana
orange
Dodamani
kiwi

'''

# 2) range() also returns the list

for i in range(1,6):
    print(i)
'''
1
2
3
4
5
'''


# 3) List Creation & comprehension
#range(1,5)-->list
l=list(range(1,5))
print(l)

#[1, 2, 3, 4]

# 4) Nested list

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])     # matrix[row][element]
#  code explain
# Accessing element → matrix[1][2]
# matrix[1] → Selects 2nd row → [4, 5, 6]
# [2] on that list → Selects 3rd element → 6
#o/p: 6




