import logging
from keyboards.keyboards import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import asyncio
from json_work.json_checker import *
from game_zone.stairs_and_sankes import *
from admin_states.user_state import *
from debug_stuff.testcube import *
from admin_states.admin_state import Change_texts_name, Change_texts, Change_step, Change_cube_roll, Change_other_texts
from debug_stuff.six_steps import * 
from postgre_work.postgre_work import *
from postgre_work.admin_postger_work import *
from json_work.json_step import * 

API_TOKEN = open('config.txt', 'r').readline()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if check_ddice(message.from_user.id) != False:
        pass
    else:
        new_ddice(message.from_user.id)
    if check_user(str(message.from_user.id)) == True:
        await message.answer(f'Вы в игре\nШаг:{get_step(str(message.from_user.id))}',
        reply_markup=game_keyboard())
    else:
        create_dice_historys_steps(message.from_user.id)
        create_dice_historys(message.from_user.id)
        text = ""
        for i in open('texts/introtext.txt', 'r', encoding='utf-8'):
            text = text + i
        if get_step(message.from_user.id) != 0:
            await message.reply(f"{text}", reply_markup=user_keyboard())


@dp.message_handler(commands=['change_other_texts'], state=None)
async def change_text(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in open('admin_list.txt', 'r').readline().split():
        await bot.send_message(message.from_user.id, 'Выберете текст, который хотите изменить:', reply_markup=change_texts1())
        await state.set_state(Change_other_texts.switch)

@dp.callback_query_handler(state=Change_other_texts.switch)
async def process_callback_kb1btn1(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.set_state(Change_other_texts.do_change)
    await state.update_data(text=callback)
    if callback == 'start_text':
        await bot.send_message(call.from_user.id, f"Текущий текст:{open('texts/introtext.txt', 'r+', encoding='utf-8').read()}", reply_markup=edit_texts1())
    elif callback == 'start_game_text':
        await bot.send_message(call.from_user.id, f"Текущий текст:{open('texts/start_new_game.txt', 'r+', encoding='utf-8').read()}", reply_markup=edit_texts1())
    elif callback == 'history_text':
        await bot.send_message(call.from_user.id, f"Текущий текст:{open('texts/history_text.txt', 'r+', encoding='utf-8').read()}", reply_markup=edit_texts1())
    elif callback == 'no_history_text':
        await bot.send_message(call.from_user.id, f"Текущий текст:{open('texts/no_history_text.txt', 'r+', encoding='utf-8').read()}", reply_markup=edit_texts1())
    elif callback == 'started_text':
        await bot.send_message(call.from_user.id, f"Текущий текст:{open('texts/start_game_text.txt', 'r+', encoding='utf-8').read()}", reply_markup=edit_texts1())
    elif callback == 'exit_text':
        await bot.send_message(call.from_user.id, f"Текущий текст:{open('texts/exit_game.txt', 'r+', encoding='utf-8').read()}", reply_markup=edit_texts1())
    elif callback == 'back':
        await state.finish()
        await bot.send_message(call.from_user.id, f"Отмена")

@dp.callback_query_handler(state=Change_other_texts.do_change)
async def process_callback_kb1btn1(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.set_state(Change_other_texts.new_text)    
    if callback == 'edit':
        await bot.send_message(call.from_user.id, f"Введите новый текст:")
    elif callback == 'back':
        await state.finish()
        await bot.send_message(call.from_user.id, f"Отмена")

@dp.message_handler(state=Change_other_texts.new_text)
async def change_other_texts(message: types.Message, state: FSMContext):
    callback = await state.get_data()
    await state.finish()
    if callback['text'] == 'start_text':
        text = message.text
        my_file = open('texts/introtext.txt', 'w', encoding='utf-8')
        my_file.write(text)
        my_file.close()
        await message.answer("Вы успешно заменили текст!")
    elif callback['text'] == 'start_game_text':
        text = message.text
        my_file = open('texts/start_new_game.txt', 'w', encoding='utf-8')
        my_file.write(text)
        my_file.close()
        await message.answer("Вы успешно заменили текст!")
    elif callback['text'] == 'history_text':
        text = message.text
        my_file = open('texts/history_text.txt', 'w', encoding='utf-8')
        my_file.write(text)
        my_file.close()
        await message.answer("Вы успешно заменили текст!")
    elif callback['text'] == 'no_history_text':
        text = message.text
        my_file = open('texts/no_history_text.txt', 'w', encoding='utf-8')
        my_file.write(text)
        my_file.close()
        await message.answer("Вы успешно заменили текст!")
    elif callback['text'] == 'started_text':
        text = message.text
        my_file = open('texts/start_game_text.txt', 'w', encoding='utf-8')
        my_file.write(text)
        my_file.close()
        await message.answer("Вы успешно заменили текст!")
    elif callback['text'] == 'exit_text':
        text = message.text
        my_file = open('texts/exit_game.txt', 'w', encoding='utf-8')
        my_file.write(text)
        my_file.close()
        await message.answer("Вы успешно заменили текст!")
    else:
        await message.answer("Что-то пошло не так!")
    


@dp.message_handler(commands=['new_text'], state=None)
async def change_text(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in open('admin_list.txt', 'r').readline().split():
        await bot.send_message(message.from_user.id, 'Введите номер клетки:')
        await state.set_state(Change_texts.id)

@dp.message_handler(commands=['new_name'], state=None)
async def change_text(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in open('admin_list.txt', 'r').readline().split():
        await bot.send_message(message.from_user.id, 'Введите номер клетки:')
        await state.set_state(Change_texts_name.id)

@dp.message_handler(state=Change_texts_name.id)
async def help(message: types.Message, state: FSMContext):
    try:
        if int(message.text) > 72:
            await state.finish()
            await bot.send_message(message.from_user.id, 'Некорректный номер клетки')
        else:
            await state.set_state(Change_texts_name.new_text)
            global new_text
            new_text = message.text
            await bot.send_message(message.from_user.id, f'Текущее название клетки:{get_step_name(int(message.text))}\nВведите новое:')
    except:
        await bot.send_message(message.from_user.id, 'Некорректный номер клетки')
        await state.finish()

@dp.message_handler(state=Change_texts_name.new_text)
async def new_number(message: types.Message, state: FSMContext):
    await state.finish()
    change_db_text_name(new_text, message.text)
    await bot.send_message(message.from_user.id, 'Вы успешно заменили название клетки!')

@dp.message_handler(commands=['off_testcube'], state=None)
async def move_test(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in open('admin_list.txt', 'r').readline().split():
        await bot.send_message(message.from_user.id, f'Значение кубика сброшено')
        off_admin(str(message.from_user.id))

@dp.message_handler(commands=['testcube'], state=None)
async def move_test(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in open('admin_list.txt', 'r').readline().split():
        await bot.send_message(message.from_user.id, f'Введите новое значение кубика:')
        await state.set_state(Change_cube_roll.roll)


@dp.message_handler(state=Change_cube_roll.roll)
async def test_move(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        if int(message.text) >= 0 and int(message.text) < 7:
            admin_on(str(message.from_user.id), int(message.text))
            await bot.send_message(message.from_user.id, text=f'Вы успешно заменили значение кубика!')
        else:
            await bot.send_message(message.from_user.id, text=f'Введены некорректные данные')
    except:
        await bot.send_message(message.from_user.id, text=f'Введены некорректные данные')

@dp.message_handler(commands=['testmove'], state=None)
async def move_test(message: types.Message, state: FSMContext):
    if str(message.from_user.id) in open('admin_list.txt', 'r').readline().split():
        await bot.send_message(message.from_user.id, f'Ваш текущий шаг:{get_step(str(message.from_user.id))}\nВведите номер клетки:')
        await state.set_state(Change_step.step)


@dp.message_handler(state=Change_step.step)
async def test_move(message: types.Message, state: FSMContext):
    await state.finish()
    try:
        if is_active(str(message.from_user.id)):
            minus_steps(str(message.from_user.id), int(message.text))
            await bot.send_message(message.from_user.id, 'Вы успешно переместились')
        else:
            await bot.send_message(message.from_user.id, 'Вы не в игре!')
    except:
        await bot.send_message(message.from_user.id, 'Некорректный номер клетки')

@dp.message_handler(state=Change_texts.id)
async def help(message: types.Message, state: FSMContext):
    try:
        if int(message.text) > 72:
            await state.finish()
            await bot.send_message(message.from_user.id, 'Некорректный номер клетки')
        else:
            await state.set_state(Change_texts.new_text)
            global new_text
            new_text = message.text
            await bot.send_message(message.from_user.id, 'Введите новый текст')
    except:
        await bot.send_message(message.from_user.id, 'Некорректный номер клетки')
        await state.finish()

@dp.message_handler(state=Change_texts.new_text)
async def new_number(message: types.Message, state: FSMContext):
    await state.finish()
    change_db_text(new_text, message.text)
    await bot.send_message(message.from_user.id, 'Вы успешно заменили текст!')


@dp.callback_query_handler(state=game_exit.answer)
async def process_callback_kb1btn1(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    callback = call.data
    if callback == 'leave':
        exit_game_(call.from_user.id)
        await bot.send_message(call.from_user.id, 'Вы вышли из игры.', reply_markup=new_user_keyboard())
    else:
        await bot.send_message(call.from_user.id, 'Отмена.')

@dp.message_handler(state=history_checker.game_id)
@dp.message_handler(state=None)
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    if check_user(str(message.from_user.id)) == True:
        if message.text == '🎲 Сделать ход':
            msg = await bot.send_dice(message.from_user.id)
            await state.set_state(dice_runed.is_runned)
            await asyncio.sleep(3.1)
            await state.finish()
            if is_admin_on(str(message.from_user.id)):
                msg.dice.value = check_admin_value(str(message.from_user.id))
            else:
                pass
            if get_step(str(message.from_user.id)) + msg.dice.value > 72:
                if msg.dice.value == 6:
                    change_ddice(str(message.from_user.id), 6)
                    await message.answer(f'Вы выбросили 6, повотрите ход', 
                     reply_markup=game_keyboard())
                    set_dices(message.from_user.id, msg.dice.value)
                    add_steps_histroy(str(message.from_user.id), "Вы вышли за рамки игрового поля, пропускаем 6", 73)
                else:
                    if is_triple_six(str(message.from_user.id)):
                        strelka = get_step(str(message.from_user.id))
                        change_step1(str(message.from_user.id), begin_place_value(str(message.from_user.id)))
                        change_step(str(message.from_user.id), msg.dice.value)
                        clear_begin_place(str(message.from_user.id))
                        create_steps_histroy(str(message.from_user.id))
                        new_ddice(str(message.from_user.id))
                        if str(get_step(str(message.from_user.id))) in stairs.keys():
                            await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИз клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда поднялись по стреле в клетку {str(stairs[str(get_step(str(message.from_user.id)))])}',
                            reply_markup=game_keyboard())
                            change_step1(str(message.from_user.id), stairs[str(get_step(str(message.from_user.id)))])                    
                        elif str(get_step(str(message.from_user.id))) in snakes.keys():
                            await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИз клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда спустились по змее в клетку {str(snakes[str(get_step(str(message.from_user.id)))])}',
                            reply_markup=game_keyboard())
                            change_step1(str(message.from_user.id), snakes[str(get_step(str(message.from_user.id)))])
                        else:
                            await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nШаг:{get_step(str(message.from_user.id))}',
                            reply_markup=game_keyboard())   
                    else:
                        await message.answer(f'Вы вышли за рамки игрового поля, бросьте кубик еще раз \nШаг:{get_step(str(message.from_user.id))}',
                        reply_markup=game_keyboard())  
                        create_steps_histroy(str(message.from_user.id))
                        clear_begin_place(str(message.from_user.id))
                        new_ddice(message.from_user.id) 
            else:
                if msg.dice.value == 6:
                    if is_begin_place(str(message.from_user.id)):
                        pass
                    else:
                        begin_place(str(message.from_user.id), get_step(str(message.from_user.id)))
                    change_ddice(message.from_user.id, msg.dice.value)
                    await message.answer('Вы выбросили 6, повотрите ход',
                     reply_markup=game_keyboard())
                    if is_predicted(str(message.from_user.id)):
                        pass
                    else:
                        strelka = get_step(str(message.from_user.id))
                        change_step(str(message.from_user.id), msg.dice.value)
                        #save_history(message.from_user.id)
                        set_dices(message.from_user.id, msg.dice.value)
                        if str(get_step(str(message.from_user.id))) in stairs.keys(): 
                            set_dices_steps(message.from_user.id, get_step(message.from_user.id)) 
                            add_steps_histroy(str(message.from_user.id), f'Из клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда поднялись по стреле в клетку {str(stairs[str(get_step(str(message.from_user.id)))])}', get_step(str(message.from_user.id)))
                            change_step1(str(message.from_user.id), stairs[str(get_step(str(message.from_user.id)))])
                            add_steps_histroy(str(message.from_user.id),f'Вы пришли в промежуточную клетку:{get_step(str(message.from_user.id))}', get_step(str(message.from_user.id)))
                        elif str(get_step(str(message.from_user.id))) in snakes.keys():
                            set_dices_steps(message.from_user.id, get_step(message.from_user.id))
                            add_steps_histroy(str(message.from_user.id), f'Из клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда спустились по змее в клетку {str(snakes[str(get_step(str(message.from_user.id)))])}', get_step(str(message.from_user.id)))
                            change_step1(str(message.from_user.id), snakes[str(get_step(str(message.from_user.id)))])
                            add_steps_histroy(str(message.from_user.id),f'Вы пришли в промежуточную клетку:{get_step(str(message.from_user.id))}', get_step(str(message.from_user.id)))

                        else:
                            add_steps_histroy(str(message.from_user.id),f'Вы пришли в промежуточную клетку:{get_step(str(message.from_user.id))}', get_step(str(message.from_user.id)))
                        set_dices_steps(message.from_user.id, get_step(message.from_user.id))
                else:
                    if is_triple_six(str(message.from_user.id)):
                        strelka = get_step(str(message.from_user.id))
                        create_steps_histroy(str(message.from_user.id))
                        minus_steps(str(message.from_user.id), begin_place_value(str(message.from_user.id)))
                        change_step(str(message.from_user.id), msg.dice.value)
                        clear_begin_place(str(message.from_user.id))
                        create_steps_histroy(str(message.from_user.id))
                        new_ddice(message.from_user.id)   
                        if is_predicted(str(message.from_user.id)):
                            delete_predict(str(message.from_user.id))
                            save_history(message.from_user.id)
                            if str(get_step(str(message.from_user.id))) in stairs.keys():
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИз клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда поднялись по стреле в клетку {str(stairs[str(get_step(str(message.from_user.id)))])}',
                                reply_markup=game_keyboard())
                                change_step1(str(message.from_user.id), stairs[str(get_step(str(message.from_user.id)))])                    
                            elif str(get_step(str(message.from_user.id))) in snakes.keys():
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИз клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда спустились по змее в клетку {str(snakes[str(get_step(str(message.from_user.id)))])}',
                                reply_markup=game_keyboard())
                                change_step1(str(message.from_user.id), snakes[str(get_step(str(message.from_user.id)))])
                            else:
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nВы пришли в клетку:{get_step(str(message.from_user.id))}',
                                reply_markup=game_keyboard())
                        else:
                            save_history(message.from_user.id)
                            new_ddice(message.from_user.id)
                            if str(get_step(str(message.from_user.id))) in stairs.keys():
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИз клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда поднялись по стреле в клетку {str(stairs[str(get_step(str(message.from_user.id)))])}',
                                reply_markup=game_keyboard())
                                change_step1(str(message.from_user.id), stairs[str(get_step(str(message.from_user.id)))])                    
                                save_history(message.from_user.id)
                            elif str(get_step(str(message.from_user.id))) in snakes.keys():
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИз клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда спустились по змее в клетку {str(snakes[str(get_step(str(message.from_user.id)))])}',
                                reply_markup=game_keyboard())
                                change_step1(str(message.from_user.id), snakes[str(get_step(str(message.from_user.id)))])
                                save_history(message.from_user.id)
                            else:
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nВы пришли в клетку:{get_step(str(message.from_user.id))}',
                                reply_markup=game_keyboard())
                    else:
                        if get_steps_history(str(message.from_user.id)) != False:
                            set_dices(message.from_user.id, msg.dice.value)
                            text1 = f"Вы выкинули комбинацию:{get_dices(message.from_user.id)}\nПромежуточные шаги:\n"
                            for i in get_steps_history(str(message.from_user.id)):
                                text1 = text1 + i[0] + f"\n"
                                if i[1] > 72:
                                    pass
                                else:
                                    pass
                                    #save_history_by_step(str(message.from_user.id), i[1], check_text(i[1]))
                            for i in get_dices_steps(message.from_user.id):
                                text1 += f"\nПоясниение к клетке {i}:\n{check_text(i)}"
                            text1 += f"\n\nСамым важным является пояснение к клетке, в которую вы пришли в конце. Но обратите внимание на промежуточные клетки, они всегда что-то означают для Вас на Вашем пути."
                        clear_begin_place(str(message.from_user.id))
                        create_dice_historys(message.from_user.id)
                        create_dice_historys_steps(message.from_user.id)
                        if is_predicted(str(message.from_user.id)):
                            new_ddice(message.from_user.id)   
                        else:
                            strelka = get_step(str(message.from_user.id))
                            change_step(str(message.from_user.id), msg.dice.value)
                            if get_steps_history(str(message.from_user.id)) != False:
                                save_history_by_step(message.from_user.id,
                                                    get_step(message.from_user.id),
                                                    text=check_text(get_step(message.from_user.id))+text1)
                            else:
                                save_history(message.from_user.id)
                            new_ddice(message.from_user.id)
                            if str(get_step(str(message.from_user.id))) in stairs.keys():
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИз клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда поднялись по стреле в клетку {str(stairs[str(get_step(str(message.from_user.id)))])}',
                                reply_markup=game_keyboard())
                                change_step1(str(message.from_user.id), stairs[str(get_step(str(message.from_user.id)))])                    
                            elif str(get_step(str(message.from_user.id))) in snakes.keys():
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИз клетки {strelka},  вы переместились в {get_step(str(message.from_user.id))}, откуда спустились по змее в клетку {str(snakes[str(get_step(str(message.from_user.id)))])}',
                                reply_markup=game_keyboard())
                                change_step1(str(message.from_user.id), snakes[str(get_step(str(message.from_user.id)))])
                            else:
                                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nВы пришли в клетку:{get_step(str(message.from_user.id))}',
                                reply_markup=game_keyboard())
                        try:
                            create_steps_histroy(str(message.from_user.id))
                            await message.answer(text=text1, reply_markup=game_keyboard())
                        except:
                            pass
            if get_step(str(message.from_user.id)) == 68 and check_ddice(str(message.from_user.id)) == 0:
                delete_predict(str(message.from_user.id))
                clear_begin_place(str(message.from_user.id))
                #save_history(message.from_user.id)
                #await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nВы пришли в клетку:{get_step(str(message.from_user.id))}')
                await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИгра окончена', reply_markup=user_keyboard())
                end_game(message.from_user.id)
            elif get_step(str(message.from_user.id)) == 68 and check_ddice(str(message.from_user.id)) != 0:
                predicted(str(message.from_user.id))
                # await message.answer(f'{check_text(int(get_step(str(message.from_user.id))))}\nИгра окончена', reply_markup=user_keyboard())
                # end_game(message.from_user.id)
        elif message.text == 'Завершить игру':
            await state.set_state(game_exit.answer)
            await message.answer(f"{open('texts/exit_game.txt', 'r+', encoding='utf-8').read()} ", reply_markup=exit_game())
            # delete_history_match(message.from_user.id)
            # extra_end_game(message.from_user.id)
            # await message.answer('Вы закончили игру.', reply_markup=user_keyboard())
    elif check_user(str(message.from_user.id)) == False:
        if message.text == 'Начать новую игру':
            text = ""
            for i in open('texts/start_new_game.txt', 'r', encoding='utf-8'):
                text = text + i
            await message.answer(f'{text}', reply_markup=user_keyboard1())
        elif message.text == 'Продолжить игру':
            entre_game(message.from_user.id)
            await message.answer(f'Вы продолжили игру с клетки:{get_step(message.from_user.id)}', reply_markup=game_keyboard())
        elif message.text == 'Посмотреть историю игр':
            if check_user_in_db(str(message.from_user.id)) == True:
                if get_games(str(message.from_user.id)) != 0:
                    await state.set_state(history_checker.game_id)
                    text = open('texts/histroy_text.txt', 'r+', encoding='utf-8').read()
                    await message.answer(f'{text}', reply_markup=switch_game(message.from_user.id))
                else:
                    text = open('texts/no_history_text.txt', 'r+', encoding='utf-8').read()
                    await bot.send_message(message.from_user.id, f"{text}")
            else:
                text = open('texts/no_history_text.txt', 'r+', encoding='utf-8').read()
                await bot.send_message(message.from_user.id, f"{text}")
        elif message.text == '🎲 Сделать ход':
            msg = await bot.send_dice(message.from_user.id)
            await state.set_state(dice_runed.is_runned)
            await asyncio.sleep(3.1)
            await state.finish()
            if is_admin_on(str(message.from_user.id)):
                msg.dice.value = check_admin_value(str(message.from_user.id))
            else:
                pass
            if msg.dice.value == 6:
                if check_user_in_db(str(message.from_user.id)) == True:
                    try:
                        extra_end_game(message.from_user.id)
                        delete_history_match(message.from_user.id)
                    except:
                        pass
                    activate_game(str(message.from_user.id))
                    #save_history(message.from_user.id)
                else:
                    create_user(str(message.from_user.id))
                text = ""
                for i in open('texts/start_game_text.txt', 'r', encoding='utf-8'):
                    text = text + i
                save_history_date(message.from_user.id)
                new_ddice(message.from_user.id)
                begin_place(str(message.from_user.id), 0)
                await message.answer(f"{text}\nВам выпало 6. Повторите ход", reply_markup=game_keyboard())
                create_steps_histroy(str(message.from_user.id))
                set_dices(message.from_user.id, msg.dice.value)
                set_dices_steps(message.from_user.id, get_step(message.from_user.id))
                add_steps_histroy(str(message.from_user.id), f"{text}, клетка:6", 6)
                #change_step(str(message.from_user.id), 6)
                #save_history(message.from_user.id)
                change_ddice(str(message.from_user.id), 6)
            else:
                await message.answer(f'Вам выпало: {msg.dice.value}.\nПовторите ход', reply_markup=user_keyboard1())
        elif message.text == 'Назад':
            await message.answer('Вы вернулись в меню', reply_markup=user_keyboard())
    

@dp.callback_query_handler(state=history_checker.game_id)
async def process_callback_kb1btn1(call: types.CallbackQuery, state: FSMContext):
    callback = call.data
    await state.finish()
    count = 0
    for i in get_match_history(call.from_user.id, int(callback)):
        text = ""
        if count == 0:
            text += f"Вы запустили игру {i[1]}\nВ процессе игры вы перемещались по клеткам:"
            count = 1
        else:
            text += f"Клетка №{i[0]}\nНаименование клетки: {get_step_name(int(i[0]))}\nПояснение к клетке:{i[1]}"
        await bot.send_message(call.from_user.id, text)
    count = 0


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)