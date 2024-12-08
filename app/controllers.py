import json

class usersController:
    @staticmethod
    def read_users(user_id:int=None) -> dict:
        with open('users.json','r') as f:
            users = json.load(f)
        if user_id != None:
            for i in range(len(users)):
                if  users[i]["id"] == user_id:
                    return users[i]
        return users
    @staticmethod
    def add_user(user:dict):
        with open('users.json','r') as f:
            users = json.load(f)
        new_id = len(users)
        for i in range(len(users)-1):
            if (users[i]["id"] + 1) != (users[i+1]["id"]):
                new_id = users[i]["id"] + 1
                break
        user["id"] = new_id
        users.append(user)
        with open('users.json','w') as f:
            json.dump(users,f)
        return "", 201
    @staticmethod
    def edit_user(user:dict,user_id):
        with open('users.json','r') as f:
            users = json.load(f)
        id_in_users = False
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                edit_user_id = i
                id_in_users = True
                break
        if id_in_users == False:
            return "", 400
        users[edit_user_id]["name"] = user["name"]
        users[edit_user_id]["lastname"] = user["lastname"]
        with open('users.json','w') as f:
            json.dump(users,f)

if __name__ == "__main__":
    controller = usersController()
    # controller.add_user({"name": "Adam", "lastname": "Taneczek"})
    controller.edit_user({"name": "Adam", "lastname": "Taneczek"},2)