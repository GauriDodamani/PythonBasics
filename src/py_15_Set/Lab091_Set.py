#Set()-> It is unordered collection of data type, with mutable and no duplicate items.
#set are in curly bracket---> {}
#



t={1,2,3,4,5,6}
print(t)  #{1, 2, 3, 4, 5, 6}

#Mixed datatype:
t1={1,2,"Gauri",3.14,True,False}     # 1=true so true gets remove as it considers duplicate value
print(t1) #{False, 1, 2, 3.14, 'Gauri'}   -> printed in unordered form


for item in t1:
   print(item)
'''
False
1
2
3.14
Gauri
'''

t1.add(10)
print(t1)
t1.remove(10)
print(t1)

empty = set()
print(type(empty))     #<class 'set'>




