# Union(OR) - Takes elements from both the sets
# | or union is used

a={1,2,3,4}
b={3,4,5,6}

print("Union of a and b set : ",a.union(b))

print(a|b)
# o/p: Union of a and b set :  {1, 2, 3, 4, 5, 6}


# Intersection(AND) - Takes only common elements from the sets
# & or intersection

a={1,2,3,4}
b={3,4,5,6}


print("Intersection of a and b is : ",a.intersection(b))
print(a&b)

# o/p: Intersection of a and b is :  {3, 4}


# Difference - Take first considered set element and remove common element

a={1,2,3,4}
b={3,4,5,6}
print("Difference of a and b set : ",a.difference(b))

print("Set A element with remove duplicate element : ",a-b)
print("Reverse for Set B element : ",b-a)


'''
Difference of a and b set :  {1, 2}
Set A element with remove duplicate element :  {1, 2}
Reverse for Set B element :  {5, 6}

'''



#Symmetric Difference - removes common elements

a={1,2,3,4}
b={3,4,5,6}


print("Symmetric difference of set A and B is : ",a^b)
#Symmetric difference of set A and B is :  {1, 2, 5, 6}