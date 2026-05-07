

def login(user):
    if user != "gauri":
        raise Exception ("Unauthorized access !!")
    return "Welcome Gauri"


#print(login("abc"))
print(login("gauri"))
