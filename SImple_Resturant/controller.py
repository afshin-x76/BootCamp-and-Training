from model import UsersInfo

user_model = UsersInfo()

class UserManagement:
    def __init__(self):
        pass

    def login_validation(self, user_name, user_pass):
        return user_model.check_user(user_name, user_pass)


    def register_validation(self, name, phone, address, password):
        pass

    def register(self, name, phone, address, password):
        username = name
        user_info = {"phone": phone, "address": address, "password": password}
        user_model.add_user(username, user_info)

    def change_info




data = {"nacho": {"name": "amir",
                  "phone": 9222222,
                  "address": "haminja",
                  "password":"1234"}}
username = "chacho"
user_info ={"name": "amir",
                  "phone": 9222222,
                  "address": "haminja",
                  "password":"1234"}
# obj1.add_user(username, user_info)
# obj1.read_users_info()