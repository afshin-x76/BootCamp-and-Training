import getpass
from controller import UserManagement

manager = UserManagement()


class ResturantApp:
    def __init__(self):
        self.state = False
        self.level = None
        self.Customer = Customer()

    def doorman(self):
        if not self.state:
            self.validating()
        else:
            pass

    def validating(self):
        print("if you want to login, please input 'login'")
        print("if you didn't registered yet and wanna to sign up, input 'signup'")
        login_cmd = input()
        if login_cmd == 'login':
            self.login()
        elif login_cmd == 'signup':
            self.signup()
        else: 
            print("please try again\n")
            self.login()

    def login(self):
        self.user_name = input("Enter your UserName: ")
        self.password = getpass.getpass("Enter your Password")
        try:
            self.level = manager.login_validation(self.user_name, self.password)
            print("Welcome Sir")
            self.state = True
            self.counter()
        except:
            print("Wrong Password Or UserName..!!")  
            self.login()
            
    def signup(self):
        user_name = input("Please input your User Name: ") 
        phone = input("Please input your phone: ")
        address = input("Please input your address: ")
        password = getpass.getpass("Please input your password: ")
        self.Customer.signup(user_name, phone, address, password)

    def logout(self):
        self.state = False
        print("Goodbye Sir...\n\n\n\n")
        self.doorman()

    def counter(self):
        cmd_prompt = input("Welcome to our Resturant Sir.\nto see the commands please input 'help': ")
        while True:
            if cmd_prompt == "help":
                print("menu         To See Foods Menu")
                print("show info    To See Your Information")
                print("change info  To Change Your Information")
                print("logout       To Logout")
            elif cmd_prompt == "menu":
                pass
            elif cmd_prompt == "show info":
                pass
            elif cmd_prompt == "change info":
                pass
            elif cmd_prompt == "logout":
                pass
            else:
                cmd_prompt = input("Wrong Command. Please Try Again: ")

    

    

        




class Person:
    def signup(self, user_name, phone, address, password):
        manager.register(user_name, phone, address, password)

    def logout(self):
        print("Goodbye Sir")

    def change_info(self):
        change_properties = dict()
        while True:
            prop = input("Which Property You wanna to change? \n exit for geting out of this secrion\n")
            if prop == ['name', 'phone', 'address']:
                change_properties[prop] = input("how do you want to change")
            elif prop = 'password':
                change_properties[prop] = getpass.getpass("please Input The new password:‌ ")
            elif prop = "exit":
                break
            else:
                print("please input ther right properties")


class Customer(Person):
    def __init__(self):
        pass


if __name__ == '__main__':
    resturantr = ResturantApp()
    resturantr.doorman()