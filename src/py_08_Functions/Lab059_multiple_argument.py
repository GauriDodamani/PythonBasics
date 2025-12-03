#Function -> Multiple argument-->displaying o/p in list

def print_mul_args(*args):
#args- List
    for i in args:
        print(i)

print_mul_args("Gauri\n")
print_mul_args("Gauri","QA\n")
print_mul_args("Gauri","Dodamani",1234567890,90.25,23*34,'\n')
print_mul_args("Gauri",12**12)



'''
O/p gets display in list format 

Gauri

Gauri
QA

Gauri
Dodamani
1234567890
90.25
782


Gauri
8916100448256

'''