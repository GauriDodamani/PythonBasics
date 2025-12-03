#Function with in the function


def f1():
    print("The f1 is called")

    def f2():
        print("The f2 is called")

    f2()

f1()