#filter :- filters the elements using a condition is True
#filter(function, iterable)


nums=[1,2,3,4,5,6]

def even_num(x):
    return x%2==0

print_even_numbers=list(filter(even_num, nums))
print(print_even_numbers)

#o/p: [2, 4, 6]  --> Only true condition will be return