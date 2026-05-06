from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def readfromexcel(self):
        pass


class Browser(ExcelReader):
    @abstractmethod
    def start(self):
        pass


    @abstractmethod
    def stop(self):
        pass


class TestCase(Browser, ExcelReader):

    def start(self):
        print("Start executing the  TC")

    def stop(self):
        print("Stop")

    def readfromexcel(self):
        print("Reading the testcase from excel")


    def runTC(self):
        self.start()
        self.readfromexcel()
        self.stop()


runner= TestCase()
runner.runTC()




#abtraction means--  hiding the most important thing and showing only basic needs or requirements
