# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import CallbackQuery
from keyboards.inline_kb import get_techsup_menu_kb, techsup_buttons_1
techsup_router = Router()

@techsup_router.callback_query(F.data == 'trouble_internet')
async def trouble_internet(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Пожалуйста, попробуйте простые действия:</b>
                                     
Шаг 1.Выключите оборудование из сети и через две минуты включите заново. 
Шаг 2.Проверьте все ли провода хорошо соединены. 
                                     
<b>В случае если проблема сохранилась, обратитесь к нам
по номеру контактного телефона поддержки
                                     
📞 88001000800
                                     
или выберите другой способ связи с нами:</b>''',
reply_markup=techsup_buttons_1())

@techsup_router.callback_query(F.data == 'trouble_internet_tv')
async def trouble_internet(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Пожалуйста, попробуйте простые действия:</b>
                                     
Шаг 1. Выключите оборудование (роутер и ТВ-приставку) из сети и через 2 минуты включите заново.
Шаг 2. Проверьте все ли провода и кабели хорошо соединены. 
Шаг 3. Выберите «правильный» источник сигнала: с помощью нажатия на кнопку A/V на пульте Ростелеком.
        
<b>В случае если проблема сохранилась, обратитесь к нам по номеру контактного телефона поддержки

📞 88001000800
                                     
или выберите другой способ связи с нами:</b>''',
reply_markup=techsup_buttons_1())

@techsup_router.callback_query(F.data == 'trouble_other')
async def trouble_internet(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
'''<b>В случае если проблема сохранилась, обратитесь к нам по номеру контактного телефона поддержки

 📞 88001000800
 
 или выберите другой способ связи с нами:</b>''',
reply_markup=techsup_buttons_1())

@techsup_router.callback_query(F.data == 'techsup_back')
async def techsup_back(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>По какой услуге ваш вопрос:</b>', 
                                     reply_markup=get_techsup_menu_kb())

    