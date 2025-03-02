from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import CallbackQuery
from keyboards.inline_kb import get_internet_tv_sim_kb, internet_tv_sim_rates_kb
internet_tv_sim_router = Router()


# подменю инлайн подключение услуги
# подменю Интернет+ТВ+sim
@internet_tv_sim_router.callback_query(F.data == 'internet_tv_sim')
async def internet_tv_sim(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Нажмите на интересующий тариф, чтобы узнать о нем подробнее:</b>',
                                     reply_markup=get_internet_tv_sim_kb())
    
@internet_tv_sim_router.callback_query(F.data == 'get_tv')
async def get_tv(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(''' Скорость до 200 мб/с 🏎️💨
Абонентская плата 595 руб. (первые 2 месяца), начиная с 3-го месяца 850 руб.
➕ видеосервис Wink (подключение на ТВ без доп.приставок) 
➕ 1 сим-карта с пакетом 1000 минут, 500 смс и 40 Гб мобильного трафика''',
reply_markup=internet_tv_sim_rates_kb())
    
@internet_tv_sim_router.callback_query(F.data == 'get_tvs')
async def get_tvs(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(''' Скорость до 200 мб/с 🏎️💨
Абонентская плата 525 руб. (первые 2 месяца), начиная с 3-го месяца 1050 руб.
➕ видеосервис Wink (подключение на ТВ без доп.приставок)
➕ до 5 сим-карт с пакетом 2000 минут, 500 смс и 40 Гб мобильного трафика''',
reply_markup=internet_tv_sim_rates_kb())
    
# к тарифам интернет+ТВ
@internet_tv_sim_router.callback_query(F.data == 'internet_tv_sim_rates')
async def internet_tv_rates(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Нажмите на интересующий тариф, чтобы узнать о нем подробнее:</b>', 
                                     reply_markup=get_internet_tv_sim_kb())