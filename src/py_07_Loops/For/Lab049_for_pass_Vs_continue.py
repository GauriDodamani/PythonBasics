for i in range(0,5,1):
    if i==3:
        pass   # do nothing
    print("Number :", i)
'''

Number : 0
Number : 1
Number : 2
Number : 3
Number : 4
'''

print("Continue")
for i in range(0,5,1):
    if i==3:
        continue   # will not print & skip to next no.
    print("Number :", i)
'''
Continue
Number : 0
Number : 1
Number : 2
Number : 4
'''