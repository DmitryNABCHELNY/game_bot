import psycopg2

conn = psycopg2.connect("dbname=db user=admin host=46.149.76.163 password=qwerty")
cur = conn.cursor()

def create_user(username):
    cur.execute(
        f"""INSERT INTO users_data (id, username, step, is_active, games_count) VALUES (1, '{username}', 6, TRUE, 0);"""
    )
    conn.commit()

def check_user(username):
    cur.execute(
            f"""SELECT id, username, step, is_active, games_count FROM public.users_data WHERE username = '{username}';"""
    )
    data = cur.fetchall()
    try:
        if data != [] and data[0][3] == True:
            return True
        else:
            return False
    except:
        return False

def check_user_in_db(username):
    try:
        cur.execute(
            f"""SELECT username FROM public.users_data WHERE username = '{username}';"""
        )
        if cur.fetchall() == []:
            return False
        return True
    except: return False

def activate_game(username):
    cur.execute(
        f"""UPDATE public.users_data SET step=6, is_active=True WHERE username = '{username}';"""
    )
    conn.commit()

def get_step(username):
    cur.execute(
            f"""SELECT step FROM public.users_data WHERE username = '{username}';"""
    )
    return cur.fetchall()[0][0]

def change_step(username, dice):
    cur.execute(
        f"""UPDATE public.users_data SET step = step+{dice} WHERE username = '{username}';"""
    )
    conn.commit()

def minus_step(username, dice):
    cur.execute(
        f"""UPDATE public.users_data SET step = step-18+{dice} WHERE username = '{username}';"""
    )
    conn.commit()

def exit_game_(username):
    cur.execute(
        f"""UPDATE public.users_data SET is_active = False WHERE username = '{username}';"""
    )
    conn.commit()

def entre_game(username):
    cur.execute(
        f"""UPDATE public.users_data SET is_active = True WHERE username = '{username}';"""
    )
    conn.commit()

def extra_end_game(username):
    cur.execute(
        f"""UPDATE public.users_data SET step = 0, is_active = False WHERE username = '{username}';"""
    )
    conn.commit()

def end_game(username):
    cur.execute(
        f"""UPDATE public.users_data SET step = 0, is_active = False, games_count = games_count+1 WHERE username = '{username}';"""
    )
    conn.commit()

def change_step1(username, num):
    cur.execute(
        f"""UPDATE public.users_data SET step = {num} WHERE username = '{username}';"""
    )
    conn.commit()

def get_games(user_id):
    cur.execute(
            f"""SELECT games_count FROM public.users_data WHERE username = '{user_id}';"""
        )
    conn.commit()
    return cur.fetchall()[0][0]
    