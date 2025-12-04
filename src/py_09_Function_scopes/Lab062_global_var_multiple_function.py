

public_toilet='PB'

def home():
    private_toilet='PT'
    print(public_toilet)
    print(private_toilet)

def stranger():
    print(public_toilet)
    #print(private_toilet)     # diff function can't access local variable

stranger()
home()




x=10

def num():
    y=5
    print(x)
    print(y)        #Only accessible inside the function

num()
print(x)
#print(y)   # local variable not accessible outside of the function

