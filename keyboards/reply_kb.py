# импортируем необходимые модули и функции
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from create_bot import admins

def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text='🚀 Подключить услуги')],
        [KeyboardButton (text='🛠️ Тех.поддержка')],
        [KeyboardButton(text='👤 Личный кабинет')],
        [KeyboardButton(text='📦 Переезд')]
    ]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text='⚙️ Управление ботом')])
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, 
                                   one_time_keyboard=True, input_field_placeholder='Выберите пункт меню:')
    return keyboard
