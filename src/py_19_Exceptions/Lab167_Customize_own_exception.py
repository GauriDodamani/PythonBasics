# create own class exception

class InvalidAgeException(Exception):       # create own exception
    pass

def drink(age):
    if age < 25 :
        raise InvalidAgeException("Invalid age of drink")   #exception replace with created own exception

print(drink(16))