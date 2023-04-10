# from pymongo import MongoClient
# client = MongoClient()

# client = MongoClient('mongodb+srv://dimkae12:Man13579qwertyy@cluster0.akrj7tv.mongodb.net/test')

# currect_db = client['db']

# collections = currect_db["text_data"]
# user_collection = currect_db["users_data"]
# history_collection = currect_db["history_data"]

# def check_text(id):
#     id = int(id)
#     return collections.find_one({"_id":id})["text"]

# def change_db_text(id, text):
#     id = int(id)
#     collections.find_one_and_update({"_id":id}, {"$set":{"text":text}})

# def save_history(user_id):
#     user_id = str(user_id)
#     user_save_data = user_collection.find_one({"username":user_id})
#     if is_in_history(int(user_save_data["step"]), int(user_save_data["games_count"])) == False:
#         history = {
#             "user_id":user_id,
#             "step":int(user_save_data["step"]),
#             "game_num":int(user_save_data["games_count"]),
#             "text":collections.find_one({"_id":int(user_save_data["step"])})["text"],
#             "photo":collections.find_one({"_id":int(user_save_data["step"])})["photo"]
#         }
#         history_collection.insert_one(history)
#     else:
#         pass

# def save_history_by_step(user_id, step, text):
#     user_id = str(user_id)
#     user_save_data = user_collection.find_one({"username":user_id})
#     if is_in_history(int(user_save_data["step"]), int(user_save_data["games_count"])) == False:
#         history = {
#             "user_id":user_id,
#             "step":step,
#             "game_num":int(user_save_data["games_count"]),
#             "text":text,
#             "photo":"photo"
#         }
#         history_collection.insert_one(history)
#     else:
#         pass

# def delete_history_match(user_id):
#     user_id = str(user_id)
#     match_id = get_match_id(str(user_id))
#     history_collection.delete_many({"user_id":user_id, "game_num":match_id})

# def is_in_history(step, match_id):
#     if history_collection.find_one({"step":step, "game_num":match_id}) != None:
#         return True
#     else:
#         return False

# def get_match_id(user_id):
#     user_id = str(user_id)
#     return user_collection.find_one({"username":user_id})["games_count"]

# def get_match_history(user_id, match_id):
#     user_id = str(user_id)
#     all_steps = []
#     for i in history_collection.find({"user_id":user_id, "game_num":match_id}):
#         all_steps.append([i["step"], i["text"]])
#     return all_steps

# def minus_steps(user_id, value):
#     user_id = str(user_id)
#     user_collection.find_one_and_update({"username":user_id}, {"$set":{"step":value}})

# def is_active(user_id):
#     user_id = str(user_id)
#     return user_collection.find_one({"username":user_id})["is_active"]