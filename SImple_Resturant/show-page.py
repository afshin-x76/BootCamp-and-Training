import getpass
from controller import UserManagement, MenuManagement

manager = UserManagement()
menu_manager = MenuManagement()


class ResturantApp:
    def __init__(self):
        self.state = False
        self.level = None
        self.cart = []

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
            self.validating()

    def login(self):
        self.user_name = input("Enter your UserName: ")
        self.password = getpass.getpass("Enter your Password: ")
        if self.user_name == "admin" and self.password == "admin":
            self.admin_room()
        else:
            self.level = manager.login_validation(self.user_name, self.password)
            if not self.level:
                self.login()
            if self.level == "admin":
                self.admin_room
            else:
                self.state = True
                self.counter()

    def signup(self):
        self.user_name = input("Please input your User Name: ") 
        phone = input("Please input your phone: ")
        address = input("Please input your address: ")
        password = getpass.getpass("Please input your password: ")
        manager.register(self.user_name, phone, address, password)
        self.counter()

    def logout(self):
        self.state = False
        self.cart = []
        print("Goodbye Sir...\n\n\n\n")
        self.validating()

    def counter(self):
        cmd_prompt = input("Welcome to our Resturant Sir.\nto see the commands please input 'help': ")
        while True:
            if cmd_prompt == "help":
                print("menu         To See Foods Menu")
                print("show info    To See Your Information")
                print("change info  To Change Your Information")
                print("logout       To Logout")
                cmd_prompt = input("input your command: ")
            if cmd_prompt == "menu":
                self.menu = menu_manager.show_menu()
                for k,v in self.menu.items():
                    print(f"food:{k}        price:{v[1]}        number:{v[0]}")
                self.add_to_cart()
            elif cmd_prompt == "show info":
                info = manager.show_info(self.user_name)
                for k,v in info.items():
                    print(f"{k}:    {v}")
                self.counter()
            elif cmd_prompt == "change info":
                self.change_info()
                self.counter()
            elif cmd_prompt == "logout":
                self.logout()
            else:
                cmd_prompt = input("Wrong Command. Please Try Again: ")
        self.counter()

    def add_to_cart(self):
        name = input("Which food you wanna to choose: (tooo go back to the counter print counter) ")
        if name == "counter":
            self.counter()
        qty = int(input(f"How many {name} do you want?: "))
        try:
            if self.menu[name][0] >= qty:
                self.menu[name][0] -= qty
                self.cart.append((name, qty))
                print("Your foods added to cart successfully")
                cmd_prompt = input("Now where do u want to go? keywords:(counter, menu, purch)")
                if cmd_prompt == "counter":
                    self.counter
                if cmd_prompt == "menu":
                    for k,v in self.menu.items():
                        print(f"food:{k}        price:{v[1]}        number:{v[0]}")
                    self.add_to_cart()
                if cmd_prompt == "purch":
                    self.purchase()
                self.counter()
            else:
                print(f"sry we don't have enough {name}")
        except:
            print(f"sry we dont have {name}")


    def purchase(self):
        menu_manager.purchase(self.user_name, self.cart)
        self.counter()

    def change_info(self):
        cmd_prompt = input("which property you wanna to change")
        if cmd_prompt in ['name', 'phone', 'address']:
            new_val = input(f"input new value for {cmd_prompt}")
            manager.change_info(self.user_name, cmd_prompt, new_val)
        elif cmd_prompt == 'password':
            new_pas = getpass.getpass("Enter Your new Password: ")
            manager.change_info(self.user_name, cmd_prompt, new_pas)
        self.counter()

    def admin_room(self):
        cmd_prompt =  input("Hello Sir. to see commands, type Help: ") 
        if cmd_prompt.lower() == "help":
            print("add user         to add a new user")
            print("rm user          to remove user")
            print("add item         add a new item to menu")
            print("remove item      remove an item from menu")
            print("increase item    increase item qunity in menu")
            print("price item       change item price")
            print("logout           to logout of the system")
            cmd_prompt = input("Now what do you want to do Sir?")
        if cmd_prompt == "add item":
            name , qty, price = (input("input food name , qty, price: ")).split()
            menu_manager.add_to_menu(name, qty, price)
        elif cmd_prompt == "remove item":
            name = input("which item you want to remove: ")
            menu_manager.remove_from_menu(name)
        elif cmd_prompt == "increase item":
            name = input("which item do you want increase: ")
            qty = int(input("How much you wanna increse that: "))
            menu_manager.increase(name, qty)
        elif cmd_prompt == "price item":
            name, price = (input("which item and how musch increase: ")).split()
            menu_manager.change_price(name, price)
        elif cmd_prompt == "logout":
            self.logout()
        else:
            print("Wrong command")
        self.admin_room()
            

if __name__ == '__main__':
    resturantr = ResturantApp()
    resturantr.validating()

