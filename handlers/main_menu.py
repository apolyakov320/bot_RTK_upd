# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from keyboards.inline_kb import main_menu_kb, privacy_menu_kb, get_services_menu_kb, get_techsup_menu_kb, relocation_kb 
start_router = Router()


# главное меню на реплай клавиатуре
@start_router.message(CommandStart())
async def cmd_start(message: Message):
     # Игнорируем команду в группах
    if message.chat.type in ['group', 'supergroup']:
        await message.answer('Для того, чтобы пользоваться командами, напишите мне в личные сообщения')
        return
    await message.answer(f'Здравствуйте, <b>{message.from_user.first_name}</b>!\nВаш id: {message.from_user.id}\n\n<b>Выберите интересующее Вас меню:</b>', 
                         reply_markup=main_menu_kb())
    
# Политика приватности
@start_router.message(Command('privacy'))
async def cmd_privacy(message: Message):
    # Игнорируем команду в группах
    if message.chat.type in ['group', 'supergroup']:
        await message.answer('Для того, чтобы пользоваться командами, напишите мне в личные сообщения')
        return
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
    
# переезд
@start_router.callback_query(F.data == 'relocation')
async def relocation(callback:CallbackQuery):
    await callback.message.edit_text('''<b>Планируете переехать на новую квартиру? 🏠 
                                     
Возьмите интернет и ТВ с собой ❗</b>
                                     
<b>Программа «Переезд»</b>
Бесплатная программа, которая позволит сохранить тот же тариф на тех же условиях при смене адреса проживания.                                      
Сохраните привычный объем опций и избавьтесь от путаницы: номер договора, баланс и бонусные баллы останутся прежними. Оборудование, взятое в аренду, остается за Вами.
                                      
<b>Приятный бонус при подключении программы – скидка 50% на 2 месяца 💰
                                     
Подать заявку на программу «Переезд» Вы можете в Личном кабинете или по номеру горячей линии</b>

📞 8-800-1000-800
 ''',
                                     reply_markup=relocation_kb())
    
# вернуться к главному меню    
@start_router.callback_query(F.data == 'back_to')
async def back_to(callback:CallbackQuery):
    await callback.message.edit_text(f'Здравствуйте, <b>{callback.from_user.first_name}</b>!\nВаш id: {callback.from_user.id}\n\n<b>Выберите интересующее Вас меню:</b>', 
                                    reply_markup=main_menu_kb())