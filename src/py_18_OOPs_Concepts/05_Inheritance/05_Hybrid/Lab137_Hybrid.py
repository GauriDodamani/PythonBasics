class BaseTest:

    def __init__(self,browser):
        self.browser = browser

    def setup(self):
        print(f"Launching {self.browser}")

class Signup(BaseTest):
    def run(self):
        self.setup()
        print("Running Signup test....\n")

class Login(BaseTest):
    def run(self):
        self.setup()
        print("Running Login test....")

s = Signup("Chrome Browser")
s.run()

l= Login("Firefox Browser")
l.run()
