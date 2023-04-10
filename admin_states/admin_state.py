from aiogram.dispatcher.filters.state import State, StatesGroup

class Change_texts(StatesGroup):
    id = State()
    new_text = State()

class Change_step(StatesGroup):
    step = State()

class Change_cube_roll(StatesGroup):
    roll = State()

class Change_cube_roll(StatesGroup):
    roll = State()

class Change_other_texts(StatesGroup):
    switch = State()
    do_change = State()
    new_text = State()

class Change_texts_name(StatesGroup):
    id = State()
    new_text = State()