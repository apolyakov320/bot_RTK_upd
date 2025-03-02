# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import Message, CallbackQuery
from keyboards.inline_kb import get_services_menu_kb, yes_no_kb
import pandas as pd
import logging


request_router = Router()

# логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# подключить 
# Состояния для сбора данных
user_data = {}

# функция сохранения данных в excel файл
def save_to_excel(user_data):
    try:
        df = pd.DataFrame.from_dict(user_data, orient='index')
        df.to_excel('Zayavki.xlsx', index=True)
    except Exception as e:
        logger.error(f"Ошибка сохранения данных в Excel: {e}")

# запрос данных
@request_router.callback_query(F.data == 'request_user_data')
async def request_user_data(callback:CallbackQuery):
    await callback.answer()
    await callback.message.answer(
'''📝<b>Пожалуйста, укажите следующие данные:</b>

Ваше ФИО (полностью, например, Иванов Иван Иванович).'''
)
    user_data[callback.from_user.id] = {} # создаем запись для пользователя  

@request_router.message()
async def process_data(message: Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        return
    
    text = message.text
    if 'ФИО' not in user_data[user_id]:
        user_data[user_id]['ФИО'] = text
        await message.answer('Спасибо! Теперь укажите адрес подключения (город, улица, дом, квартира).')
    elif 'Адрес' not in user_data[user_id]:
        user_data[user_id]['Адрес'] = text
        await message.answer('Отлично! Теперь укажите Ваш номер телефона (в формате +7XXXXXXXXXX или 8XXXXXXXXXX)')
    elif 'Телефон' not in user_data[user_id]:
        user_data[user_id]['Телефон'] = text
        await message.answer(
f'''<b>Проверьте введенные данные:</b> 
ФИО: {user_data[user_id]['ФИО']}
Адрес: {user_data[user_id]['Адрес']}
Телефон: {user_data[user_id]['Телефон']}

Всё верно?
''', reply_markup=yes_no_kb()
        )

# нажатие кнопки да
@request_router.callback_query(F.data == 'accept')
async def accept(callback:CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    logger.info(f"Пользователь {user_id} ввел данные.")
    save_to_excel(user_data)
    if user_id in user_data:
        del user_data[user_id]  # Очищаем данные пользователя
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
    await callback.message.edit_text('<b>Хочу подключить:</b>', 
                                   reply_markup=get_services_menu_kb())