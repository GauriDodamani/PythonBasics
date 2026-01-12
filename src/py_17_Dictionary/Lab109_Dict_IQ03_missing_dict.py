dict1={"a":1,"b":2,"c":3}
dict2={"a":1,"b":2}

# missing_dict= dict1-dict2
# print(missing_dict)


missing_dict=set(dict1.keys()-dict2.keys())
print(missing_dict)
