
name=input("enter your name :")
print(name)
print(type(name))

#What is String-> it is a bunch of char
# In Python single character is also a string datatype

a='h'  #single-quote
b="i"  #double quotes
print(a,b)
print(type(a))
print(type(b))

'''
o/p:
h i
<class 'str'>
<class 'str'>

'''

#len()-> counts the string , length will always start counting from 1 and not zero(0)

name=input("enter your name :")
print(name)
print(type(name))
print(len(name))   #len of the string
print(name.upper()) #GAURI in uppercase
print(name.lower()) #gauri in lowercase

'''
o/p:
enter your name :Gauri Dodamani
Gauri Dodamani
<class 'str'>
14
'''