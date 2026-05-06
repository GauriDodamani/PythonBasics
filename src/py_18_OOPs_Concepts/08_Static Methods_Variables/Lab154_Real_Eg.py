
class ExcelReader:

    @staticmethod
    def readfromexcel():
        print("Reading from excel")


class MySQLDBConnection:
    @staticmethod
    def readSQLFile():
        print("Reading from SQL file")


class TC:

    def runTC(self):
        ExcelReader.readfromexcel()
        MySQLDBConnection.readSQLFile()
        print("No need to create function. \n")

class UpdatedTC:

    def runTC(self):
        ExcelReader.readfromexcel()
        MySQLDBConnection.readSQLFile()
        print("Updated TC are executed ")


t=TC()
t.runTC()
t1=UpdatedTC()
t1.runTC()

