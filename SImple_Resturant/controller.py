from model import UsersInfo, Foods
from view import UserMessages, MenuMessages

user_model = UsersInfo()
food_model = Foods()
user_msg = UserMessages()
menu_msg = MenuMessages()

class UserManagement:
    def __init__(self):
        pass

    def login_validation(self, user_name, user_pass):
        if user_model.check_user(user_name, user_pass):
            user_msg.login_successful()
            return True
        else:
            user_msg.login_failed()
            return False

    def register_validation(self, name, phone, address, password):
        pass

    def register(self, name, phone, address, password):
        username = name
        user_info = {"phone": phone, "address": address, "password": password, "level":"C1", "past_buy":[]}
        if user_model.add_user(username, user_info):
            user_msg.register_successfully()
            return True
        else:
            user_msg.register_fail()
            return False

    def change_info(self, username,prop, new_val):
        if user_model.change_info(username, prop, new_val):
            user_msg.info_update()
            return True
        else:
            user_msg.info_update_fail
            return False
    
    def show_info(self, user):
        return user_model.read_user_info(user)



class MenuManagement:
    def add_to_menu(self, name, qty, price):
        food_info = [int(qty), int(price)]
        food_model.add_to_menu(name,food_info)
        menu_msg.add_food()
        return True

    def remove_from_menu(self, name):
        if food_model.remove(name):
            menu_msg.rm_food()
        else:
            menu_msg.rm_food_fail()

    def increase(self, name, qty):
        food_model.increase(name, qty)
        menu_msg.item_increase()
        return True

    def add_to_cart(self,name, qty):
        if food_model.decrease(name, qty):
            menu_msg.add_to_cart()
            return True
    
    def show_menu(self):
        foods = food_model.read_menu
        return foods
        
    def change_price(self, name, price):
        food_model.change_price(name, price)
        
    def purchase(self,user ,cart):
        price = food_model.decrease(cart)
        menu_msg.purch_su()
        user_model.change_info(user, "past_buy", price)
        return True
