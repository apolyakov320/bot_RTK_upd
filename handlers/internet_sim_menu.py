from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import CallbackQuery
from keyboards.inline_kb import internet_sim_kb, internet_tv_sim_kb, get_services_menu_kb
internet_sim_router = Router()

# подменю инлайн подключение услуги
# подменю Интернет+Sim
@internet_sim_router.callback_query(F.data == 'internet_sim')
async def internet_sim(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Тариф "Технология общения"</b>
Скорость до 200 мб/с 🏎️💨
Абонентская плата 375 руб. (первые 2 месяца), начиная с 3-го месяца 750 руб.
➕ Sim-карта 40 ГБ/1000 минут/500 СМС

<b>Тариф "Технология Общения. Семейный"</b>
Скорость до 200 мб/с 🏎️💨
Абонентская плата 475 руб. (первые 2 месяца), начиная с 3-го месяца 950 руб.
➕ видеосервис Wink (подключение на ТВ без доп.приставок)
➕ до 5 Sim-карт с пакетом 40 Гб/2000 минут/500 СМС''', 
                                    reply_markup=internet_sim_kb())

# добавить услугу ТВ = Интернет - ТВ - Sim 
@internet_sim_router.callback_query(F.data == 'need_tv_sim')
async def internet_tv_sim(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Тариф "Технология выгоды"</b>
Скорость до 200 мб/с 🏎️💨
Абонентская плата 450 руб. (первые 2 месяца), начиная с 3-го месяца 900 руб.
➕ видеосервис Wink (подключение на ТВ без доп.приставок) 
➕ Sim-карта 40 ГБ/1000 минут/500 СМС
                                     
<b>Тариф "Технология выгоды. Семейный"</b>
Скорость до 200 мб/с 🏎️💨
Абонентская плата 550 руб. (первые 2 месяца), начиная с 3-го месяца 1100 руб.
➕ видеосервис Wink (подключение на ТВ без доп.приставок)
➕ до 5 Sim-карт с пакетом 40 Гб/2000 минут/500 СМС''',
                                     reply_markup=internet_tv_sim_kb())
    
# вернуться к меню подключение услуги
@internet_sim_router.callback_query(F.data == 'back_to_services')
async def back_to_services(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Выберите интересующий Вас вариант из списка ниже: </b>',
                                     reply_markup=get_services_menu_kb()) 