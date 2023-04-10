from aiogram.dispatcher.filters.state import State, StatesGroup

class dice_runed(StatesGroup):
    is_runned = State()
    
class history_checker(StatesGroup):
    game_id = State()

class game_exit(StatesGroup):
    answer = State()