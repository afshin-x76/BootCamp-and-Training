import json
from pathlib import Path
import pickle

BASE_DIR = Path("./Training/SImple_Resturant")
USER_DATABASE = BASE_DIR / "users-information.json"
FOOD_DATABASE = BASE_DIR / "food_menu.json"

class UsersInfo:
    __instance = None
    
    def __init__(self):
        self.users = dict()
        self.keys = ['password', 'phone', 'address', 'level', 'past_buy']

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(*args, **kwargs)
        return cls.__instance
    
    def add_user(self, username, user_info):
        if self.data_validation(user_info):
            load_file = self.read_users_info
            load_file[username] = user_info
            with open(USER_DATABASE, "r+") as user_file:
                json.dump(load_file, user_file)
        return True

    @property
    def read_users_info(self):
        try:
            with open(USER_DATABASE, "r") as user_file:
                return json.load(user_file)
        except:
            return dict()

    def data_validation(self, info):  
        for i in info:
            if i not in self.keys:
                return False
        return True

    def check_user(self, username, password):
        load_file = self.read_users_info
        if username in load_file:
            if load_file[username]["password"] == password:
                return load_file[username]["level"]
        return False

    def change_info(self, username,prop, new_val):
        load_file = self.read_users_info
        if prop != "past_buy":
            load_file[username][prop] = new_val
        else:
            load_file[username][prop] += new_val
        with open(USER_DATABASE, "w") as user_file:
            json.dump(load_file, user_file)
            return True
    
    def read_user_info(self, user):
        load_file = self.read_users_info
        return load_file[user]



        
class Foods:
    def add_to_menu(self,name, food_info):
        load_file = self.read_menu
        with open(FOOD_DATABASE, "w") as food_file:
            load_file[name] = food_info
            json.dump(load_file, food_file)
            return True
    
    @property
    def read_menu(self):
        with open(FOOD_DATABASE, "r") as food_file:
            return json.load(food_file)


    def remove(self, name):
        load_file = self.read_menu
        try: load_file.remove(name)
        except: return False
        with open(Foods, "w") as food_file:
            json.dump(load_file, food_file)
            return True

    def increase(self, name, qty):
        load_file = self.read_menu
        load_file[name][0] += qty
        with open(FOOD_DATABASE, "w") as food_file:
            json.dump(load_file, food_file)
            return True


    def change_price(self, name, price):
        load_file = self.read_menu
        load_file[name][1] += price
        with open(FOOD_DATABASE, "w") as food_file:
            json.dump(load_file, food_file)
            return True


    def decrease(self, cart):
        load_file = self.read_menu
        total_price = 0
        for k,v in cart:
            load_file[k][0] -= v
            total_price += load_file[k][1] * v
        with open(FOOD_DATABASE, "w") as food_file:
            json.dump(load_file, food_file)
        return total_price


if __name__ == '__main__':
    obj1 = UsersInfo()
    obj2 = UsersInfo()
    print(obj1)
    print(obj2)

