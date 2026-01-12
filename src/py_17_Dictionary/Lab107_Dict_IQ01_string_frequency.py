# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string.


#logic building
#i/p:  string="automation"
#o/p: {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}


string=input("\nEnter the string : \n")

char_count={}

for char in string:
    print(char)
    char_count[char]=char_count.get(char,0)+1

print(char_count)


'''
Enter the string : 
automation
a
u
t
o
m
a
t
i
o
n
{'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}
'''