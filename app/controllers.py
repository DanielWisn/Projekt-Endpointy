import json

class usersController:
    @staticmethod
    def read_users(user_id:int=None) -> dict:
        with open('./app/users.json','r') as f:
            users = sorted(json.load(f), key=lambda x: x["id"])
        if user_id != None:
            for i in range(len(users)):
                if  users[i]["id"] == user_id:
                    return users[i],200
        return users, 200
    @staticmethod
    def add_user(user:dict):
        with open('./app/users.json','r') as f:
            users = sorted(json.load(f), key=lambda x: x["id"])
        new_id = len(users)
        for i in range(len(users)-1):
            if (users[i]["id"] + 1) != (users[i+1]["id"]):
                new_id = users[i]["id"] + 1
                break
        user["id"] = new_id
        users.append(user)
        with open('./app/users.json','w') as f:
            json.dump(users,f)
        return "", 201
    @staticmethod
    def edit_user(user:dict,user_id:int):
        try:
            if user["lastname"] == None or user["name"] == None:
                return "", 400
        except:
            return "",400
        with open('./app/users.json','r') as f:
            users = sorted(json.load(f), key=lambda x: x["id"])
        id_in_users = False
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                edit_user_id = i
                id_in_users = True
                break
        if id_in_users == False:
            return "", 400
        try:
            users[edit_user_id]["name"] = user["name"]
            users[edit_user_id]["lastname"] = user["lastname"]
            with open('./app/users.json','w') as f:
                json.dump(users,f)
            return "", 204
        except:
            return "",400
    @staticmethod
    def put_user(user:dict,user_id:int):
        with open('./app/users.json','r') as f:
            users = sorted(json.load(f), key=lambda x: x["id"])
        id_in_users = False
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                id_in_users = True
                break
        user["id"] = user_id
        if id_in_users == False:
            users.append(user)
            with open('./app/users.json','w') as f:
                json.dump(users,f)
            return "", 204
        elif id_in_users == True:
            users[user_id]["name"] = user["name"]
            users[user_id]["lastname"] = user["lastname"]
            with open('./app/users.json','w') as f:
                json.dump(users,f)
            return "",204
    @staticmethod
    def delete_user(user_id:int):
        with open('./app/users.json','r') as f:
            users = sorted(json.load(f), key=lambda x: x["id"])
        id_in_users = False
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                delete_user_id = i
                id_in_users = True
                break
        if id_in_users == False:
            return "",400
        elif id_in_users == True:
            users.pop(delete_user_id)
            with open('./app/users.json','w') as f:
                json.dump(users,f)
            return "", 204