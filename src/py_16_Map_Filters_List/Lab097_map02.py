names= ["gauri" , "dodamani" , "riya" , "vrinda"]

#define function
def upper_case(string):
    return string.upper()

#calling function
upper_case_names=list(map(upper_case,names))
print(upper_case_names)

#o/p: ['GAURI', 'DODAMANI', 'RIYA', 'VRINDA']
