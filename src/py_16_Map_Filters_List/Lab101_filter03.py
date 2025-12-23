names=["Gauri","","Dodamani","","QA Tester"]

def no_empty(x):
    if x != "":
        return True
    return None


print_no_empty=list(filter(no_empty,names))
print(print_no_empty)


#o/p: ['Gauri', 'Dodamani', 'QA Tester']


# lambda--> one line code
print_no_empty=list(filter(lambda x: x!="", names))
print(print_no_empty)


