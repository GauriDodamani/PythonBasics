#Function -> Keyword arguments

def display_information(name,role):   # parameter-> name,role
    print(f"Name is : {name} , Role is : {role}")

display_information("Gauri","QA")
display_information(name="Gauri1",role="QA1")
display_information(role="QA2",name="Gauri2")  # keyword argument name=, role=



def multiple_args(fname="A",lname="B"):
    print(f"Multiple arguments : {fname} , {lname}")

multiple_args()     #no arugment pass take parameter variable defined value.
multiple_args(fname="Gauri",lname="Dodamani")
multiple_args(fname="Gauri")
multiple_args(lname="Dodamani")
multiple_args(lname="Dodamani",fname="Gauri")

'''
o/p:

Multiple arguments : A , B
Multiple arguments : Gauri , Dodamani
Multiple arguments : Gauri , B
Multiple arguments : A , Dodamani
Multiple arguments : Gauri , Dodamani

'''
