#Multiple Inhertiance : Child class inherits from multiple Parent classes


class APIBase:
    def auth_api(self):
        print("Authentication API")

class DBBase():
    def db_connect(self):
        print("Connecting to DB")

class TestHybrid(APIBase , DBBase):
    def run(self):
        self.auth_api()
        self.db_connect()
        print("Testing")

obj=TestHybrid()
obj.run()