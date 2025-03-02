# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.reply_kb import main_kb
from keyboards.inline_kb import get_services_menu_kb, lk_kb, get_techsup_menu_kb
start_router = Router()


# меню старт
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Здраствуйте, <b>{message.from_user.first_name}</b>!\nЯ интерактивный помощник по услугам компании Ростелеком.\nВыберите интересующее Вас меню.', 
                         reply_markup=main_kb(message.from_user.id))
    
# главное меню на реплай клавиатуре
# меню подключить услугу
@start_router.message(F.text == '🚀 Подключить услуги')
async def get_services(message: Message):
    await message.answer('<b>Хочу подключить:</b>', 
                         reply_markup=get_services_menu_kb())

# меню тех.поддержка
@start_router.message(F.text == '🛠️ Тех.поддержка')
async def techsup(message: Message):
    await message.answer('<b>По какой услуге ваш вопрос:</b>', 
                         reply_markup=get_techsup_menu_kb())  
    
# меню личный кабинет
@start_router.message(F.text == '👤 Личный кабинет')
async def lk(message: Message):
    await message.answer('<b>Здесь вы можете управлять своими данными и услугами:</b>', 
                         reply_markup=lk_kb()) 
      
# меню переезд
@start_router.message(F.text == '📦 Переезд')
async def get_your_bot(message: Message):
    await message.answer
