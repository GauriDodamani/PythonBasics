# Right Triangle (For Loop)
# *
# **
# ***
# ****
# *****

#n=5
#hint: i>j

rows = int(input(" Enter the no.of rows for right angle triangle "))

for i in range(1,rows+1):
    for j in range(i):
        print("*",end="")
    print()