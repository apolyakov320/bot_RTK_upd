# импортируем необходимые модули и функции
from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import CallbackQuery
from keyboards.inline_kb import get_internet_tv_kb, internet_tv_rates_kb
internet_tv_router = Router()


# подменю инлайн подключение услуги
# подменю Интернет+ТВ
@internet_tv_router.callback_query(F.data == 'internet_tv')
async def internet_tv(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Нажмите на интересующий тариф, чтобы узнать о нем подробнее:</b>',
                                     reply_markup=get_internet_tv_kb())

# подменю тариф «Технология развлечения. Онлайн»
@internet_tv_router.callback_query(F.data == 'get_tro')
async def get_tro(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Скорость до 200 мб/с 🏎️💨\nАбонентская плата 375 руб. (первые 2 месяца), начиная с 3-го месяца 750 руб.\n➕ видеосервис Wink',
                                     reply_markup=internet_tv_rates_kb())
    
# подменю тариф «Технология развлечения»
@internet_tv_router.callback_query(F.data == 'get_tr')
async def get_tr(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Скорость до 200 мб/с 🏎️💨\nАбонентская плата 375 руб. (первые 2 месяца), начиная с 3-го месяца 750 руб.\n➕ видеосервис Wink (требуется ТВ-приставка)',
                                     reply_markup=internet_tv_rates_kb())
    
# к тарифам интернет+ТВ
@internet_tv_router.callback_query(F.data == 'internet_tv_rates')
async def internet_tv_rates(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('<b>Нажмите на интересующий тариф, чтобы узнать о нем подробнее:</b>', 
                                     reply_markup=get_internet_tv_kb())
  


    
