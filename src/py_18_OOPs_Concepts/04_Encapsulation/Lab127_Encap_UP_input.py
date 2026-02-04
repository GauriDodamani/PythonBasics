class LoginPage:



    def __init__(self,user_email,user_password):
        self.email = user_email
        self.password = user_password

    def login_confirm(self):
        if self.email == "gauri@gmail.com" and self.password == "Gauri123":
            print("Allowed,Login Success")
        else:
            print("Login Failed")

# user input
email = input("Enter the email : ")
password = input("Enter the password : ")

#create object ref & calling the method(inside the class)
confirmation = LoginPage(email,password)
confirmation.login_confirm()
