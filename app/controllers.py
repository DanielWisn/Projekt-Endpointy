import json

class usersController:
    @staticmethod
    def read_users(numerek:int=None) -> dict:
        with open('users.json','r') as f:
            wartosc = json.load(f)
        if numerek != None:
            return wartosc[numerek]
        return wartosc
    def add_user(user:dict) -> None:
        with open('users.json','wr') as f:
            wartosc = json.load(f)
            wartosc.update(user)