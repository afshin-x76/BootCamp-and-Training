class UserMessages:
    def login_successful(self):
        print("Login Successfull")

    def login_failed(self):
        print("Login Failed. Please Try Again")

    def register_successfully(self):
        print("Sign up successful")

    def register_fail(self):
        print("Sign up failed")

    def info_update(self):
        print("Information Successfully Updated")
    
    def info_update_fail(self):
        print("Information Update failed")

class MenuMessages:
    def add_food(self):
        print("Item added")

    def rm_food(self):
        print("Item removed from menu")

    def rm_food_fail(self):
        print("Item doesn't exist in menu")

    def item_increase(self):
        print("item increased successfuly")

    def add_to_cart(self):
        print("item added to cart successfuly")

    def purch_su(self):
        print("Purchase Successful")