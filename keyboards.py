from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage


greet_kb_5 = ReplyKeyboardMarkup(keyboard=[ 
    [KeyboardButton(text = 'Начать')]
    
],
            resize_keyboard=True,
            one_time_keyboard = True)


greet_kb1 = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text ="Далее")],
        
],
                                resize_keyboard=True,
                                one_time_keyboard = True)

greet_kb2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text ="Посмотреть")]
],
        resize_keyboard=True)

inline_kb1 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text = 'Нажми!', callback_data='But_1')]
])

inline_kb2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text = 'Дальше', callback_data='But_2')]
])

inline_kb3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Нажми!', callback_data='Bye')]
])

inline_kb4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='But_4')]
])

inline_kb5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Другие функции', callback_data='But_5')]
])

inline_kb6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дальше', callback_data='But_6')]
])

inline_kb7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дальше', callback_data='But_7')]
])

inline_kb8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дальше', callback_data='But_8')]
])

inline_url = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Или так", url="https://github.com")]
])

inline_kb_full = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Или так", url="https://github.com")],
    [InlineKeyboardButton(text='Дальше', callback_data='But_6')],
]
                                      )
# Создаем кнопки
#inline_btn_6 = )
#inline_url = InlineKeyboardButton(text='ии так', url='https://github.com')

# Создаем клавиатуру
#inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_url, inline_btn_6)
#= InlineKeyboardMarkup(row_width=1).add(inlane_url, inline_btn_6)
















