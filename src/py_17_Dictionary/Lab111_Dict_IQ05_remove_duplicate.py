#  Remove duplicate values from a dictionary.
#if duplicate values appears it will take first value and not the second value
dict={"a":10,"b":15,"c":10,"d":20}


unique_value = set()
result ={}

for key, value in dict.items():
    if value not in unique_value:
        result[key]=value
        unique_value.add(value)

print(result)