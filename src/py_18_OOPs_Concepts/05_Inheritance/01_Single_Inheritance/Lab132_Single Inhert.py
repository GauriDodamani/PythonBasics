#Single Inheritance: A child class gets all assest from Prarent class

class BaseTest:
    driver = "Chrome"
    __driver1 = "Edge"

    def setup(self):
        print(f"Base setup with the browser and env : {self.__driver1}")

class LoginTest(BaseTest):
    __driver1 = "Edge"

    def run(self):
        self.setup()
        print(f"Running the login test : {self.driver} ")

obj=LoginTest()
obj.run()

