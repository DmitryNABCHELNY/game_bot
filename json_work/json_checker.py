import json
from mongo_work.admin_mongo_work import *

def check_ddice(username):
    with open('json_work/db.json') as f:
        templates = json.load(f)
        if str(username) in list(templates.keys()):
            return templates[str(username)]
        else:
            return False

def new_ddice(username):
    with open('json_work/db.json') as f:
        users = json.load(f)
        with open('json_work/db.json', 'w') as f:
            users[str(username)] = 0
            f.write(json.dumps(users))

def change_ddice(username, dice):
    with open('json_work/db.json') as f:
        users = json.load(f)
        users[str(username)] = users[str(username)] + dice
        with open('json_work/db.json', 'w') as f1:
            f1.write(json.dumps(users))

def change_ddice1(username):
    with open('json_work/db.json') as f:
        users = json.load(f)
        users[str(username)] = users[str(username)] - 6
        with open('json_work/db.json', 'w') as f1:
            f1.write(json.dumps(users))

def is_triple_six(username):
     with open('json_work/db.json') as f:
        templates = json.load(f)
        if str(username) in list(templates.keys()):
            if templates[str(username)] == 18:
                return True
            else:
                return False

def triple_six(username):
    minus_steps(user_id=username, value=18)

def predicted(username):
    with open('json_work/predicted_win.json') as f:
        users = json.load(f)
        with open('json_work/predicted_win.json', 'w') as f:
            users[str(username)]=True
            f.write(json.dumps(users))

def is_predicted(username):
    with open('json_work/predicted_win.json') as f:
        users = json.load(f)
        if str(username) in list(users.keys()):
            return True
        else:
            return False

def delete_predict(username):
    with open('json_work/predicted_win.json') as f:
        users = json.load(f)
        try:
            del users[str(username)]
            with open('json_work/predicted_win.json', 'w') as f:
                f.write(json.dumps(users))
        except:
            pass
        
def begin_place(username, step):
    with open('json_work/begin_place.json') as f:
        users = json.load(f)
        with open('json_work/begin_place.json', 'w') as f:
            users[str(username)]=step
            f.write(json.dumps(users))

def begin_place_value(username):
    with open('json_work/begin_place.json') as f:
        users = json.load(f)
        return users[str(username)]

def is_begin_place(username):
    with open('json_work/begin_place.json') as f:
        users = json.load(f)
        if str(username) in list(users.keys()):
            return True
        else:
            return False

def clear_begin_place(username):
    with open('json_work/begin_place.json') as f:
        users = json.load(f)
        try:
            del users[str(username)]
            with open('json_work/begin_place.json', 'w') as f:
                f.write(json.dumps(users))
        except:
            pass
       
        