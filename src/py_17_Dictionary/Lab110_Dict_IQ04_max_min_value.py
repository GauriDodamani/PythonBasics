# function that returns the maximum value from a dictionary.
# {"a": 10, "b": 20, "c": 30}

dict={"a":10,"b":20,"c":30}

def min_value(dictionary):
    return min(dictionary.values())

print(min_value(dict))

def max_value(dictionary):
    return max(dictionary.values())
print(max_value(dict))