from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from postgre_work.postgre_work import * 


def user_keyboard():
    but1 = KeyboardButton('Начать новую игру')
    but2 = KeyboardButton('Посмотреть историю игр')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(but1).add(but2)
    return keyboard

def new_user_keyboard():
    but1 = KeyboardButton('Начать новую игру')
    but3 = KeyboardButton('Продолжить игру')
    but2 = KeyboardButton('Посмотреть историю игр')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(but1).add(but2)
    keyboard.add(but3)
    return keyboard

def user_keyboard1():
    but1 = KeyboardButton('🎲 Сделать ход')
    but2 = KeyboardButton('Назад')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(but1, but2)
    return keyboard

def game_keyboard():
    but1 = KeyboardButton('🎲 Сделать ход')
    but2 = KeyboardButton('Завершить игру')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(but1).add(but2)
    return keyboard

def switch_game(user_id):
    user_id = str(user_id)
    user_data = get_games(user_id)
    if user_data == 0:
        keyboard = InlineKeyboardMarkup()
    else:
        keyboard = InlineKeyboardMarkup()
        for i in range(user_data):
            but = InlineKeyboardButton(text=f"🎯Игра {i+1}", callback_data=str(i))
            keyboard.insert(but)
    return keyboard

def change_texts1():
    but1 = InlineKeyboardButton('Текст после команды: /start', callback_data='start_text')
    but2 = InlineKeyboardButton('Текст перед стартом игры', callback_data='start_game_text')
    but3 = InlineKeyboardButton('Текст если есть история игр', callback_data='history_text')
    but4 = InlineKeyboardButton('Текст если история игр отсутствует', callback_data='no_history_text')
    but5 = InlineKeyboardButton('Текст при старте игры', callback_data='started_text')
    but7 = InlineKeyboardButton('Текст при попытке покинуть игру', callback_data='exit_text')
    but6 = InlineKeyboardButton('Отмена', callback_data='back')
    keyboard = InlineKeyboardMarkup().add(but1)
    keyboard.add(but2)
    keyboard.add(but5)
    keyboard.add(but4)
    keyboard.add(but3)
    keyboard.add(but7)
    keyboard.add(but6)
    return keyboard

def edit_texts1():
    but1 = InlineKeyboardButton('Редактировать✏️', callback_data='edit')
    but2 = InlineKeyboardButton('Отмена❌', callback_data='back')
    keyboard = InlineKeyboardMarkup().add(but1)
    keyboard.add(but2)
    return keyboard

def exit_game():
    but1 = InlineKeyboardButton('Покинуть игру', callback_data='leave')
    but2 = InlineKeyboardButton('Отмена', callback_data='back')
    keyboard = InlineKeyboardMarkup().add(but1)
    keyboard.add(but2)
    return keyboard