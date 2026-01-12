#Dict-->
#1. Key-value pair
#2. Unordered, mutable, indexed
#3. Curly ->{}
#4. Used in-> API Automation(JSON, Dict)


my_dict={
    "name" : "Gauri",
    "age" : 30,
    "role" : "QA Tester",
    "experience" : 4
}

print(my_dict)
#o/p: {'name': 'Gauri', 'age': 30, 'role': 'QA Tester', 'experience': 4}

#get value
print(my_dict["name"]) #o/p: Gauri
print(my_dict.get("role"))

#change value
my_dict["role"]="Software Engineer"
print(my_dict)
#o/p: {'name': 'Gauri', 'age': 30, 'role': 'Software Engineer', 'experience': 4}

#del any key value
del my_dict["age"]
print(my_dict)
#o/p: {'name': 'Gauri', 'role': 'Software Engineer', 'experience': 4}

del my_dict["experience"]
print(my_dict)


my_dict["age"]=67
print(my_dict)
#o/p: {'name': 'Gauri', 'role': 'Software Engineer', 'experience': 4, 'age': 67}

#iteration key value
for key, value in my_dict.items():
    print (key,value)

'''
o/p: 

name Gauri
role Software Engineer
experience 4
age 67
'''
#True / False

print("age" in my_dict)  #True
print("experience" in my_dict)  #False