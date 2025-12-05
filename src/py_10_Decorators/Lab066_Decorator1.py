
def before_after_test(func):
    def wrapper():
        print("Before running the test")
        func()
        print("After running the test")

    return wrapper()


@before_after_test
def test_ui():
    print("I am testing a UI Test")

#test_ui()      -> if want to call the function-> then write return wrapper & not return wrapper()
