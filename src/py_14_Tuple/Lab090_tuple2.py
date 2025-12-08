cities=("Pune","Mumbai","Hyderabad","Bangalore")
print(len(cities))     #4
print("Baramati" in cities) #False
print("Mumbai" in cities)   #True
# cities.append("Mangalore")  #AttributeError: 'tuple' object has no attribute 'append'
# print(cities)


api_url=("abc.com/get", "pqr.com/put", "xyz.com/post")
print(api_url[1])


colors = ("red", "green", "blue")
for c in colors:
    print(c)

'''
red
green
blue
'''


number=(12,15)*3
print(number) #(12, 15, 12, 15, 12, 15)

name= "Gauri" *2
print(name)  #GauriGauri


nums = (13, 20, 20, 33, 20,45,98,76)
print(len(nums))
print(nums.count(20))
print(nums.index(45))



my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)    # (1, 2, 3)

back_to_list = list(my_tuple)
print(back_to_list)   # [1, 2, 3]
print(max(back_to_list))   # [1, 2, 3]

my_list = [1, 2, 3]
print(my_list[0:2])
print(my_list[-1])