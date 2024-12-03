from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Регистрация')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

kb_i = InlineKeyboardMarkup()
but1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
but2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
but3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
but4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb_i.row(but1, but2, but3, but4)
