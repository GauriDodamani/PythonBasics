#List-> it a collection of items

a=[1,20,93,44,57,6,20,7]   #only int data type
b=['apple','banana','orange','strawberry','kiwi']       #only str data type
c=[1234,'fruit',3.14,True]      #mixed data type

print(a)            #prints the list
print(type(b))      # gives data type <class 'list'>
print(len(c))       #gives the length of list
print(c[1])         #element of index 1 -> fruit
print(a.count(20))  # counts how many times passed value occurs -> 2
#print(a.sort())    # does not return the sorted list.   .sort() modifies a list but returns None
a.sort()
print(a)
#or another way to sort
print(sorted(a))


#reverse sort
a.sort(reverse=True)
print(a)

#or
a.reverse()
print(a)

#max/min/sum

print(max(a))
print(min(a))
print(sum(a))

b = list("Gauri")  #converting the string into list by a character
print(b)           # ['G', 'a', 'u', 'r', 'i']

#empty list
list=[]
print(list)        #[]

#❌ No, you cannot reverse a string using sort() directly.
# ✔ sort() works on lists only
# ❌ Not on strings
# ✔ Sorting rearranges items in alphabetical order
# ❌ Reversing means opposite order, not sorting order

# list("bye") → ['b', 'y', 'e']
# sorted(...) → ['b', 'e', 'y']
#
#
# That is not reversed → reversed is ['y', 'e', 'b']
#
# So sorting cannot guarantee reverse order of original string.




# a=list((1,2,3,4,5,"apple",'fruit'))   #converting tuple into list
# print(a)
