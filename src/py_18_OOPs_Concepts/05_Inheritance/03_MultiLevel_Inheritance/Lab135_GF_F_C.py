class TestSuite:
    def info(self):
        print("GrandFather")

class BaseSuite(TestSuite):
    def setup(self):
        print("Father")

class UITest(BaseSuite):
    def run(self):
        self.info()
        self.setup()
        print("Son")


obj=UITest()
obj.run()