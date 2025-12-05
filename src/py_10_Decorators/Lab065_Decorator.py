#used mostly in api 7 web automation

#Decorators: add extra functionality to an existing function without modifying its original code.
# 1. Modify the behavior of the function w/o changing the original code
# 2. It is powerful tool that wraps another function w/o changing the original code

#wrapper (): we can use any other name but initially using a wrapper gets more clear about the concept
#(gift wrap)



def add_security(func):

    def wrapper():                  #by default wrapper function need to use
        print("Before driving the scooter")
       # print("We need to check : Helmet,licence, gloves, keys, scooter")
        func()
        print("After driving the scooter")
        #print("We need to check :Battery power, Park properly, lock scooter, Remove key")

    return wrapper


#drive_ola_scooter = add_security(drive_ola_scooter) this works same as @add_security
@add_security           #decorator
def drive_ola_scooter():
    print("I am driving ola scooter")

drive_ola_scooter()


@add_security
def drive_chetak_scooter():
   print("I am driving chetak scooter")

drive_chetak_scooter()







#another prgm:

# def log_decorator(func):
#     def wrapper():
#         print(f"📍 Starting: {func.__name__}")
#         func()
#         print(f"✔ Finished: {func.__name__}\n")
#     return wrapper
#
# @log_decorator
# def test_api():
#     print("Testing API...")
#
# test_api()
#


