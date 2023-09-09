import asyncio
import logging
import datetime
from datetime import timedelta
import random


#aiogram и всё утилиты для коректной работы с Telegram API
from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.fsm.context import FSMContext
text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#конфиг с настройками
import config
from db import BotDB
import os.path


#задаём логи
logging.basicConfig(level=logging.INFO)


#инициализируем бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

db = BotDB('people.db')

@dp.message_handler(commands=['start'],state='*')
async def start(message: types.Message):
    button_start = KeyboardButton('Старт')

    start = ReplyKeyboardMarkup(one_time_keyboard=True)

    start.add(button_start)
    await message.answer('Добро пожаловать в MISIS знакомства',reply_markup=start)
    if(not db.user_exists(message.from_user.id)):
        await message.answer('Вижу, ты тут в первый раз, давай создадим тебе анкету') #проверить!!!!!!!
        await message.answer('Введи ')
        # user_id, photo, description, username, course, institute, interests

        db.add_user()




class CreateProfile(StatesGroup):
    name = State()
    description = State()
    course = State()
    institute = State()
    interests = State()
    photo = State()


# hendler для старта создания профиля
@dp.message_handler(lambda message: message.text == "Создать анкету",state = '*')
async def create_profile(message : types.Message):

    button_cancel = KeyboardButton('Выйти')

    menu_exit = ReplyKeyboardMarkup()

    menu_exit.add(button_cancel)

    if message.from_user.username != None:
        if(not db.user_exists(message.from_user.id)):
            await message.answer('Как можно тебя называть')
            await CreateProfile.name.set()
        elif(db.user_exists(message.from_user.id)):
            await message.answer('У тебя уже есть анкета')
    else:
        await message.answer('У вас не заполнен username в телеграме')


#hendler для ввода имени
@dp.message_handler(state=CreateProfile.name)
async def input_profile_name(message: types.Message, state: FSMContext):
    if str(message.text) == 'Выйти'
        await state.finish()
        await start(message)
        return
    if len(str(message.text)) < 35:
        await state.update_data(profile_name = message.text.lower())
        await message.answer('Теперь заполни описание своего профиля')
        await CreateProfile.next()
    else:
        await message.answer('Попробуй ещё раз!')
        return

@dp.message_handler(state=CreateProfile.description)
async def input_profile_description(message: types.Message, state: FSMContext):
    if str(message.text) == 'Выйти':
        await state.finish()
        await start(message)
        return
    if len(message.text) < 35:
        await state.update_data(profile_description=message.text)
        await message.answer('')
        await CreateProfile.next()
    else:
        await message.answer('Попробуй ещё раз!')
        #прерывание функции
        return



