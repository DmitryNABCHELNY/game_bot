# from pymongo import MongoClient
# client = MongoClient()

# client = MongoClient('mongodb+srv://dimkae12:Man13579qwertyy@cluster0.akrj7tv.mongodb.net/test')

# currect_db = client['db']

# collections = currect_db["users_data"]

# def create_user(username):
#     username = str(username)
#     new_user = {"username":username,
#     "step":6,
#     "is_active":True,
#     "games_count":0}
#     collections.insert_one(new_user)

# def check_user(username):
#     username = str(username)
#     for i in collections.find():
#         if i['username'] == username and i['is_active'] == True:
#             return True
#     return False

# def check_user_in_db(username):
#     username = str(username)
#     for i in collections.find():
#         if i['username'] == username:
#             return True
#     return False

# def activate_game(username):
#     username = str(username)
#     collections.find_one_and_update({"username":username}, {"$set":{"step":0, "is_active":True}})

# def get_step(username):
#     username = str(username)
#     return collections.find_one({"username":username})["step"]

# def change_step(username, dice):
#     username = str(username)
#     collections.find_one_and_update({"username":username},
#      {"$set":{"step":collections.find_one({"username":username})["step"]+dice}})

# def minus_step(username, dice):
#     username = str(username)
#     collections.find_one_and_update({"username":username},
#      {"$set":{"step":collections.find_one({"username":username})["step"]-18+dice}})

# def extra_end_game(username):
#     username = str(username)
#     collections.find_one_and_update({"username":username},
#      {"$set":{"step":1, "is_active":False}})

# def end_game(username):
#     username = str(username)
#     collections.find_one_and_update({"username":username},
#      {"$set":{"step":1, "is_active":False,
#       "games_count":collections.find_one({"username":username})["games_count"]+1}})

# def change_step1(username, num):
#     username = str(username)
#     collections.find_one_and_update({"username":username},
#      {"$set":{"step":num}})

# def get_games(user_id):
#     user_id = str(user_id)
#     return collections.find_one({"username":user_id})["games_count"]
# # ins_result = collections.find({"username":1})
# # for i in ins_result:
# #     print(i)

