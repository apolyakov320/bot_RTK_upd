# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import CallbackQuery
from keyboards.inline_kb import internet_tv_kb, get_services_menu_kb
internet_tv_router = Router()


# подменю инлайн подключение услуги
# подменю Интернет+ТВ
@internet_tv_router.callback_query(F.data == 'internet_tv')
async def internet_tv(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Тариф "Технология развлечения. Онлайн"</b>
Скорость до 200 мб/с 🏎️💨
Абонентская плата 375 руб. (первые 2 месяца), начиная с 3-го месяца 750 руб.
➕ видеосервис Wink(подключение на ТВ без доп.приставок)
                                     
<b>Тариф "Технология развлечения"</b>
Скорость до 200 мб/с 🏎️💨
Абонентская плата 375 руб. (первые 2 месяца), начиная с 3-го месяца 750 руб.
➕ видеосервис Wink(необходима ТВ-приставка, приобретается отдельно)''',
                                    reply_markup=internet_tv_kb())
    
# вернуться к меню подключение услуги
@internet_tv_router.callback_query(F.data == 'back_to_services')
async def back_to_services(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Выберите интересующий Вас вариант из списка ниже: </b>',
                                     reply_markup=get_services_menu_kb())  
  


    
