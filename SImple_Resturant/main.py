import getpass
class Person:
    def __init__(self, name):
        self.name = name
        self.state = False

    def login(self):
        while True:
            self.username = input("Enter Your UserName: ")
            self.password = getpass.getpass(prompt="Password: ")
            if self.username in db:
                if self.username.password == self.password:
                    print("welcome")
                    break
                else:
                    print("wrong Password")
            else:
                print("wrong UserName")
        self.state = True

            
            

class Admin(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def add_to_menu(self, name, price, qty):
        pass

    def remove_from_menu(self, name):
        pass

class Customer(Person):
    def __init__(self, name, phpne, addres):
        super().__init__(name)
        self.addres = addres
        self.phone = phone
        self.past_buy = dict()

    # def change_info(self, **kwargs):
    #     info = 
    #     for item in kwargs.keys():


