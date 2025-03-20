# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import Message, CallbackQuery
from keyboards.inline_kb import enter_data_kb, get_services_menu_kb, yes_no_kb
import pandas as pd
import re
import logging



request_router = Router()

# логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# подключить 
# Состояния для сбора данных
user_data = {}

# Функция для проверки номера телефона
def validate_phone(phone: str) -> bool:
    """
    Проверяет, соответствует ли номер телефона формату:
    - +7XXXXXXXXXX или 8XXXXXXXXXX (X - цифры)
    - Длина номера: 11 символов.
    """
    pattern = re.compile(r'^(\+7|8)\d{10}$')  # Регулярное выражение для проверки
    return bool(pattern.match(phone))

# функция сохранения данных в excel файл
def save_to_excel(user_data):
    try:
        df = pd.DataFrame.from_dict(user_data, orient='index')
        df.to_excel('Zayavki.xlsx', index=True)
    except Exception as e:
        logger.error(f"Ошибка сохранения данных в Excel: {e}")

# ввод номера/назад

@request_router.callback_query(F.data == 'enter_data')
async def enter_data(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Чтобы узнать подробнее о выбранном Вами тарифе, пожалуйста, позвоните по номеру:</b>
                                     
📞 +73452599936 
                                     
<b>или оставьте свой номер для связи и мы Вам обязательно перезвоним</b>''',
reply_markup=enter_data_kb())

# запрос данных
@request_router.callback_query(F.data == 'request_user_data')
async def request_user_data(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
'''<b>Пожалуйста, введите номер в формате +7XXXXXXXXXX или 8XXXXXXXXXX(где Х - цифры).
Напишите "отмена" для возврата в прошлое меню</b>'''
)
    user_data[callback.from_user.id] = {} # создаем запись для пользователя  
    
@request_router.message(F.text.lower() == "отмена")  # Обработка команды "отмена"
async def cancel_handler(message: Message):
    user_id = message.from_user.id
    if user_id in user_data:
        del user_data[user_id]  # Удаляем данные пользователя

    await message.answer(
        '''<b>Чтобы узнать подробнее о выбранном Вами тарифе, пожалуйста, позвоните по номеру:</b>

📞 +73452599936

<b>или оставьте свой номер для связи, и мы Вам обязательно перезвоним</b>''',
        reply_markup=enter_data_kb()
    )

@request_router.message(F.text)  # Обработка ввода номера телефона
async def process_data(message: Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        return

    phone = message.text

    if validate_phone(phone):  # Если номер корректен, сохраняем его
        user_data[user_id]['Телефон'] = phone
        await message.answer(
            f'''<b>Проверьте введенные данные:</b>
Телефон: {user_data[user_id]['Телефон']}

Всё верно?''',
            reply_markup=yes_no_kb()
        )
    else:
        # Если номер некорректен, запрашиваем повторный ввод
        await message.answer('''<b>Номер телефона введен в неправильном формате. 
Пожалуйста, введите номер в формате +7XXXXXXXXXX или 8XXXXXXXXXX(где Х - цифры).
Напишите "отмена" для возврата в прошлое меню</b>'''
        )

# нажатие кнопки да
@request_router.callback_query(F.data == 'accept')
async def accept(callback:CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    logger.info(f"Пользователь {user_id} ввел данные.")
    save_to_excel(user_data)
    await callback.message.edit_text('''😊 Спасибо за Ваш интерес, проявленный к услугам Ростелекома.
👨‍💻В ближайшее время с Вами свяжется специалист
                                     
Ростелеком - это:
🏎️💨 оптика в квартиру: скорость интернета не зависит от числа пользователей в доме
🖥️ умная система мониторинга сети решит проблему с интернетом до того, как она возникнет у Вас 
🛡️ современная система обнаружения атак обезопасит Ваши данные'''
                                     )

# нажатие кнопки нет   
@request_router.callback_query(F.data == 'decline') 
async def decline(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Чтобы узнать подробнее о выбранном Вами тарифе, пожалуйста, позвоните по номеру:</b>
                                     
📞 +73452599936 
                                     
<b>или оставьте свой номер для связи и мы Вам обязательно перезвоним</b>''',
reply_markup=enter_data_kb())