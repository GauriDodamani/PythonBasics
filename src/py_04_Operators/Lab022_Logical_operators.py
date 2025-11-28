#Logical operator-> Performs AND, OR & NOT operation returns value in True & False
#Used to combine conditional statement

a , b = 5 , 10

#AND operator  -> only value is 11->True otherwise all value are False
print("and operator: ")
print(a<0 and b<0)
print(a<0 and b>1)
print(a>1 and b<0)
print(a>1 and b>1)

print("or operator: ")
#OR operator  -> Only value is 00-> False otherwise all value are True
print(a<0 or b<0)
print(a<0 or b>1)
print(a>1 or b<0)
print(a>1 or b>1)


#NOT operator -> When value is True it will return False vs.
print("not operator: ")
print(not(a>0))   #5>0-> True but o/p will be false
