# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import CallbackQuery
from keyboards.inline_kb import get_internet_kb, internet_rates_kb
internet_router = Router()


# подменю инлайн подключение услуги
# подменю Интернет
@internet_router.callback_query(F.data == 'internet')
async def internet(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Нажмите на интересующий тариф, чтобы узнать о нем подробнее:</b>',
                                     reply_markup=get_internet_kb())

# подменю Тариф «Технология доступа»
@internet_router.callback_query(F.data == 'get_td')
async def get_td(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Скорость до 200 мб/с 🏎️💨\nАбон.плата 300 руб.(первые 2 месяца), начиная с 3-го месяца 600 руб.',
                                     reply_markup=internet_rates_kb())
    
# подменю Тариф «Технология общения»
@internet_router.callback_query(F.data == 'get_to')
async def get_to(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Скорость до 200 мб/с 🏎️💨\nАбон.плата 525 руб.(первые 2 месяца), начиная с 3-го месяца 750 руб.\n➕ 1 сим-карта с пакетом 1000 минут, 500 смс и 40 Гб мобильного трафика.',
                                     reply_markup=internet_rates_kb())
    
# к тарифам интернет
@internet_router.callback_query(F.data == 'internet_rates')
async def internet_rates(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Нажмите на интересующий тариф, чтобы узнать о нем подробнее:</b>', 
                                     reply_markup=get_internet_kb())