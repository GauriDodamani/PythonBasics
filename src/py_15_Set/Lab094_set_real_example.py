set1=set(["Gauri","Vinit","Gauri.."])  # set()-> converts list to set
print(set1)        #{'Gauri', 'Gauri..', 'Vinit'}
print(len(set1))    # 3

#printing list of items one by one

for item in set1:
    print(item)

'''
Gauri
Gauri..
Vinit
'''

set1.add("Working")
print(set1)
# {'Gauri', 'Gauri..', 'Vinit', 'Working'}

set1.remove("Gauri..")
print(set1)

# {'Working', 'Vinit', 'Gauri'}