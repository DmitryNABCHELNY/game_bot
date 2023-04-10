import json

def admin_on(username, value):
    with open('debug_stuff/cube_nuber.json') as f:
        users = json.load(f)
        with open('debug_stuff/cube_nuber.json', 'w') as f:
            users[str(username)] = value
            f.write(json.dumps(users))

def is_admin_on(username):
    with open('debug_stuff/cube_nuber.json') as f:
        users = json.load(f)
        if str(username) in list(users.keys()) and check_admin_value(username) != 0:
            return True
        else:
            return False

def check_admin_value(username):
    with open('debug_stuff/cube_nuber.json') as f:
        users = json.load(f)
        return users[str(username)]

def off_admin(username):
    with open('debug_stuff/cube_nuber.json') as f:
        users = json.load(f)
        with open('debug_stuff/cube_nuber.json', 'w') as f:
            users[str(username)] = 0
            f.write(json.dumps(users))