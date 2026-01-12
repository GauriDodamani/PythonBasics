#when having same key but latest value will be taken

student_info={
    "name" : "Gauri",
    "age" : 25,
    "age" :30,
    "address" : "MH"
}

print(student_info)
print(student_info["name"])
print(student_info["age"])
student_info["age"]=50
print(student_info)


'''
o/p: 
{'name': 'Gauri', 'age': 30, 'address': 'MH'}
Gauri
30
{'name': 'Gauri', 'age': 50, 'address': 'MH'}

'''