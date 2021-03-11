import json
from pathlib import Path

BASE_DIR = Path("./Training/SImple_Resturant")
USER_DATABASE = BASE_DIR / "users-information.json"


class UsersInfo:
    __instance = None
    
    def __init__(self):
        self.users = dict()
        self.keys = ['name', 'password', 'phone', 'address']

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(*args, **kwargs)
        return cls.__instance
    
    def add_user(self, username, user_info):
        if self.data_validation(user_info):
            load_file = self.read_users_info
            load_file[username] = user_info
            with open(USER_DATABASE, "w") as user_file:
                json.dump(load_file, user_file)

    @property
    def read_users_info(self):
        with open(USER_DATABASE, "r") as user_file:
            return json.load(user_file)
            

    def data_validation(self, info):  
        for i in info:
            if i not in self.keys:
                return False
        return True

    def check_user(self, username, password):
        load_file = self.read_users_info
        if username in load_file:
            if load_file[username]["password"] == password:
                return True
        return False

        

if __name__ == '__main__':
    obj1 = UsersInfo()
    obj2 = UsersInfo()
    print(obj1)
    print(obj2)

