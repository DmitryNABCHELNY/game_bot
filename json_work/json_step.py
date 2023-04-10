import json

def create_dice_historys(username):
    with open('json_work/watch_steps.json') as f:
        users = json.load(f)
        with open('json_work/watch_steps.json', 'w') as f:
            users[str(username)] = ""
            f.write(json.dumps(users))

def set_dices(username, step):
    with open('json_work/watch_steps.json') as f:
        users = json.load(f)
        with open('json_work/watch_steps.json', 'w') as f:
            users[str(username)] = users[str(username)] + f"{str(step)} "
            f.write(json.dumps(users))

def get_dices(username):
    with open('json_work/watch_steps.json') as f:
        users = json.load(f)
        return ", ".join(users[str(username)].split())


def create_dice_historys_steps(username):
    with open('json_work/steps_wth.json') as f:
        users = json.load(f)
        with open('json_work/steps_wth.json', 'w') as f:
            users[str(username)] = ""
            f.write(json.dumps(users))

def set_dices_steps(username, step):
    with open('json_work/steps_wth.json') as f:
        users = json.load(f)
        with open('json_work/steps_wth.json', 'w') as f:
            users[str(username)] = users[str(username)] + f"{str(step)} "
            f.write(json.dumps(users))

def get_dices_steps(username):
    with open('json_work/steps_wth.json') as f:
        users = json.load(f)
        return users[str(username)].split()
