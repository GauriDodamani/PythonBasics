class BaseTest:
    def info(self):
        print("Setup from BaseTest --> Father ")

class Signup(BaseTest):
    def run(self):
        print("Running for Signup --> Child1 \n")


class Login(BaseTest):
    def run(self):
        print("Running for Login --> Child2 ")


obj1=Signup()
obj1.info()
obj1.run()


obj2=Login()
obj2.info()
obj2.run()