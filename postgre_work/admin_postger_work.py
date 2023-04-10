import psycopg2
import datetime

conn = psycopg2.connect("dbname=db user=admin host=46.149.76.163 password=qwerty")
cur = conn.cursor()

def check_text(id):
    id = int(id)
    cur.execute(
        f"""SELECT text_ FROM public.text_data WHERE id = {id};"""
    )
    return cur.fetchone()[0]
    
def change_db_text(id, text):
    id = int(id)
    cur.execute(
        f"""UPDATE text_data SET text_='{text}' WHERE id = {id};"""
    )
    conn.commit()

def change_db_text_name(id, text):
    id = int(id)
    cur.execute(
        f"""UPDATE text_data SET text_name='{text}' WHERE id = {id};"""
    )
    conn.commit()

def save_history(user_id):
    cur.execute(
        f"""SELECT * FROM public.users_data WHERE username = '{user_id}';"""
    )
    data = cur.fetchall()
    if is_in_history(data[0][2], data[0][4]) == False:
        get_text = f"""SELECT text_ FROM text_data WHERE id = {data[0][2]}"""
        cur.execute(
            f"""INSERT INTO history_data (id, user_id, step, game_num, text_) VALUES (1, '{user_id}', {data[0][2]}, {data[0][4]}, ({get_text}));"""
        )
        conn.commit()
    else:
        pass


def is_in_history(step, match_id):
    if cur.execute(
        f"""SELECT step FROM public.history_data WHERE (step = {step}) AND (game_num = {match_id});"""
        ) != None:
        return True
    else:
        return False


def save_history_by_step(user_id, step, text):
    cur.execute(
        f"""SELECT * FROM public.users_data WHERE username = '{user_id}';"""
    )
    data = cur.fetchall()
    cur.execute(
        f"""INSERT INTO history_data (id, user_id, step, game_num, text_) VALUES (1, '{user_id}', {step}, {data[0][4]}, '{text}');"""
    )
    conn.commit()

def save_history_date(user_id):
    cur.execute(
        f"""SELECT * FROM public.users_data WHERE username = '{user_id}';"""
    )
    data = cur.fetchall()
    cur.execute(
        f"""INSERT INTO history_data (id, user_id, step, game_num, text_) VALUES (1, '{user_id}', 0, {data[0][4]}, '{datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}');"""
    )
    conn.commit()

def delete_history_match(user_id):
    match_id = get_match_id(user_id)
    cur.execute(
        f"""DELETE FROM history_data WHERE (game_num = {match_id}) AND (user_id = '{user_id}');"""
    )
    conn.commit()

def get_match_id(user_id):
    cur.execute(
        f"""SELECT games_count FROM public.users_data WHERE username = '{user_id}';"""
    )
    return cur.fetchone()[0]
    
def get_match_history(user_id, match_id):
    all_steps = []
    cur.execute(
        f"""SELECT * FROM public.history_data WHERE (user_id = '{user_id}') AND (game_num = {match_id});"""
    )
    for i in cur.fetchall():
        all_steps.append([i[2], i[4]])
    return all_steps

def minus_steps(user_id, value):
    cur.execute(
        f"""UPDATE users_data SET step = {value} WHERE username = '{user_id}';"""
    )
    conn.commit()

def is_active(user_id):
    cur.execute(
        f"""SELECT is_active FROM users_data WHERE username = '{user_id}'"""
    )
    return cur.fetchall()[0][0]
    
def get_step_name(id):
    cur.execute(
        f"""SELECT text_name FROM text_data WHERE id = '{id}'"""
    )
    return cur.fetchall()[0][0]

# for i in range(72):
#     cur.execute(
#         f"""INSERT INTO text_data (id, text_, text_name) VALUES ({i+1}, 'Текст из БД', 'Без Названия');"""
#     )
#     conn.commit()