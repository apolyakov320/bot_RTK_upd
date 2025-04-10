# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import CallbackQuery
from keyboards.inline_kb import get_techsup_menu_kb, get_techsup_lk_kb, techsup_social_kb
techsup_router = Router()

@techsup_router.callback_query(F.data == 'trouble_internet')
async def trouble_internet(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Пожалуйста, попробуйте простые действия:</b>
                                     
1️⃣. Выключите оборудование из сети и через две минуты включите заново.
                                      
2️⃣. Проверьте все ли провода хорошо соединены. 
                                     
<b>В случае, если проблема сохранилась, обратитесь к нам на горячую линию</b>
                                     
📞 8-800-1000-800
                                     
<b>или самостоятельно оставьте заявку в Личном кабинете:</b>''',
reply_markup=get_techsup_lk_kb())

@techsup_router.callback_query(F.data == 'trouble_internet_tv')
async def trouble_internet(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Пожалуйста, попробуйте простые действия:</b>
                                     
1️⃣. Выключите оборудование (роутер и ТВ-приставку) из сети и через две минуты включите заново.
                                     
2️⃣. Проверьте все ли провода и кабели хорошо соединены. 
                                     
3️⃣. Выберите «правильный» источник сигнала: с помощью нажатия на кнопку A/V на пульте Ростелеком.
        
<b>В случае, если проблема сохранилась, обратитесь к нам на горячую линию</b>
                                    
📞 8-800-1000-800
                                     
<b>или самостоятельно оставьте заявку в Личном кабинете:</b>''',
reply_markup=get_techsup_lk_kb())

@techsup_router.callback_query(F.data == 'trouble_other')
async def trouble_internet(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
'''<b>По прочим вопросам обращайтесь к нам на горячую линию:</b>

📞 8-800-1000-800

<b>или напишите сообщение в социальных сетях, мы обязательно разберемся и поможем ❤️</b>''',
reply_markup=techsup_social_kb())

@techsup_router.callback_query(F.data == 'techsup_back')
async def techsup_back(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>По какой услуге ваш вопрос:</b>', 
                                     reply_markup=get_techsup_menu_kb())

    