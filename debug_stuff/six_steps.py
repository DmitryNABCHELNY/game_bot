import json

def create_steps_histroy(username):
    with open('debug_stuff/history.json', encoding='utf-8') as f:
        users = json.load(f)
        with open('debug_stuff/history.json', 'w') as f:
            users[str(username)] = []
            f.write(json.dumps(users))

def add_steps_histroy(username, value, step):
    with open('debug_stuff/history.json', encoding='utf-8') as f:
        users = json.load(f)
        with open('debug_stuff/history.json', 'w', encoding='utf-8') as f:
            users[str(username)].append([value, step])
            f.write(json.dumps(users))

def get_steps_history(username):
    with open('debug_stuff/history.json', encoding='utf-8') as f:
        users = json.load(f)
        if str(username) in list(users.keys()):
            if users[str(username)] != []:
                return users[str(username)]
        return False

