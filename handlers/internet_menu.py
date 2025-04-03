# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import CallbackQuery
from keyboards.inline_kb import internet_kb, internet_sim_kb, internet_tv_kb, get_services_menu_kb
internet_router = Router()


# подменю инлайн подключение услуги
# подменю Интернет
@internet_router.callback_query(F.data == 'internet')
async def internet(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Тариф "Технология доступа"</b>
Скорость до 200 мб/с 🏎️💨
Абон.плата 300 руб.(первые 2 месяца), начиная с 3-го месяца 600 руб.
                                     
<b>Тариф "Игровой"</b>
Скорость до 500 мб/с 🏎️💨
Абон.плата 950 руб.''',
                                     reply_markup=internet_kb())
    
# добавить услугу ТВ
@internet_router.callback_query(F.data == 'need_tv')
async def need_tv(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('''<b>Тариф "Технология развлечения. Онлайн"</b>
Скорость до 200 мб/с 🏎️💨
Абонентская плата 375 руб. (первые 2 месяца), начиная с 3-го месяца 750 руб.
➕ видеосервис Wink(работает без ТВ-приставки)
                                     
<b>Тариф "Технология развлечения"</b>
Скорость до 200 мб/с 🏎️💨
Абонентская плата 375 руб. (первые 2 месяца), начиная с 3-го месяца 750 руб.
➕ видеосервис Wink(необходима ТВ-приставка, приобретается отдельно)''',
                                     reply_markup=internet_tv_kb())
    
# добавить услугу Sim-карта
@internet_router.callback_query(F.data == 'need_sim')
async def need_tv(callback:CallbackQuery):
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

# вернуться к меню подключение услуги
@internet_router.callback_query(F.data == 'back_to_services')
async def back_to_services(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Выберите интересующий Вас вариант из списка ниже: </b>',
                                     reply_markup=get_services_menu_kb()) 