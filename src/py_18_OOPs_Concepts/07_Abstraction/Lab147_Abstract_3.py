from abc import ABC, abstractmethod

class BrowserManager(ABC):
    def __init__(self, browser):
        self.browser = browser

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("We know when to stop the search")


class ChromeBrowser(BrowserManager):
    def start(self):
        print("Let start the browser with chrome")

tc = ChromeBrowser("chrome")
tc.start()
tc.stop()