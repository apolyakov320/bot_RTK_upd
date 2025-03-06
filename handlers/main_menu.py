# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from keyboards.inline_kb import main_menu_kb, get_services_menu_kb, get_techsup_menu_kb, review_kb, privacy_menu_kb
start_router = Router()


# главное меню на реплай клавиатуре
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Здравствуйте, <b>{message.from_user.first_name}</b>!\n\n<b>Выберите интересующее Вас меню:</b>', 
                         reply_markup=main_menu_kb())
    
# Политика приватности
@start_router.message(Command('privacy'))
async def cmd_privacy(message: Message):
    await message.answer('<b>Политика конфиденциальности доступна по кнопке ниже:</b>', 
                         reply_markup=privacy_menu_kb())
    
# выбор пункта меню на реплай клавиатуре
# подключить услуги
@start_router.callback_query(F.data == 'connect_services')
async def connect_services(callback:CallbackQuery):
    await callback.message.edit_text('<b>Выберите интересующий Вас вариант из списка ниже: </b>',
                                     reply_markup=get_services_menu_kb())

# тех.поддержка
@start_router.callback_query(F.data == 'techsup')
async def techsup(callback:CallbackQuery):
    await callback.message.edit_text('<b>Пожалуйста, выберите категорию: </b>',
                                     reply_markup=get_techsup_menu_kb())
    
# поблагодарить сотрудника
@start_router.callback_query(F.data == 'thanks_to')
async def thanks_to(callback:CallbackQuery):
    await callback.message.edit_text('''<b>Мы рады, что смогли вам помочь!
                                     
Пожалуйста, поделитесь вашим мнением о специалисте — ваш отзыв вдохновляет нашу команду и помогает нам расти.</b>''',
reply_markup=review_kb())

# вернуться к главному меню    
@start_router.callback_query(F.data == 'back_to')
async def back_to(callback:CallbackQuery):
    await callback.message.edit_text(f'Здравствуйте, <b>{callback.from_user.first_name}</b>!\n\n<b>Выберите интересующее Вас меню:</b>', 
                                    reply_markup=main_menu_kb())
       