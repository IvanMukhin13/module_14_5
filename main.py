import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from config import *
from keyboards import *
import texts
from crud_functions import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# Стартовая команда /start
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Добро пожаловать, {message.from_user.username} ' + texts.start, reply_markup=start_kb)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer(texts.about)
    await message.answer()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'files/{i}.png', 'rb') as f:
            await message.answer_photo(f, get_all_products('Product_db.db')[i-1])
    await message.answer(text='Выберите продукт для покупки:', reply_markup=kb_i)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


# Функция для начала регистрации
@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await RegistrationState.username.set()
    await message.reply("Введите имя пользователя (только латинский алфавит):")


# Обработчик для состояния username
@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if not is_included(username):
        await state.update_data(username=username)
        await RegistrationState.email.set()
        await message.reply("Введите свой email:")
    else:
        await message.answer("Пользователь существует, введите другое имя.")


# Обработчик для состояния email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    email = message.text
    await state.update_data(email=email)
    await RegistrationState.age.set()
    await message.reply("Введите свой возраст:")


# Обработчик для состояния age
@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    age = message.text
    user_data = await state.get_data()
    username = user_data['username']
    email = user_data['email']

    add_user(username, email, age)
    await message.answer("Регистрация завершена!")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
