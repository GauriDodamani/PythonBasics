#1 - Create .env (dotenv)file
#2 - Go to Terminal, enter--> pip install dotenv
#3 import load_dotenv & os
#4 load_dotenv ()
#5 os.getenv()
# pip-> is package manager of python, dotenv --> library name which read the (credential/ secure data) from .env file

# https://pypi.org/project/python-dotenv/    detail pip file


from dotenv import load_dotenv  #created by python community--> import by using from
import os                       #created by python guys--> can be directly imported

class LoginPage:


    def __init__(self,user_email,user_password):

        self.email = user_email
        self.password = user_password

    def login_confirm(self):

        load_dotenv()                   # reads variables from a .env file and sets them in os.environments


        #(os.getenv("USERNAME)---> it is consider as windows Username & password rename it with other variable name)
        if self.email == os.getenv("APP_USERNAME") and self.password == os.getenv("APP_PASSWORD"):
            print("Allowed, Login Success")
        else:
            print("Login Failed")


email = input("Enter the vwo login email ")
password = input("Enter the vwo login password ")

vwo_object_ref = LoginPage(email,password)
vwo_object_ref.login_confirm()

print("For Windows : ",os.name)
