from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


try:
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.find_element("id","not exists button")


except NoSuchElementException as nse:           #nse:NoSuchElement
    print("Element not found ", nse.msg)
