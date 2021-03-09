import json


class UsersInfo:
    __instance = None
    def __init__(self):
        if UsersInfo().__instance != None:
            