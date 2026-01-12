#zip function is used to get key values

keys=["name", "age", "address","role"]
values=["Gauri", 30,"PU"]

my_dict= dict(zip(keys, values))
print(my_dict)


#merge 2 dictionary

dict1={"a":1,"b":2,"c":3}
dict2={"d":4,"e":5,"f":6}

merge_dict= dict1|dict2
print(merge_dict)
print(merge_dict.get("e"))