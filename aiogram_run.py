# импортируем необходимые модули и функции
import asyncio
from create_bot import bot, dp, scheduler
from handlers.main_menu import start_router 
from handlers.techsup_menu import techsup_router
from handlers.request_data import request_router
from handlers.internet_menu import internet_router
from handlers.internet_tv_menu import internet_tv_router
from handlers.internet_sim_menu import internet_sim_router
from handlers.internet_tv_sim_menu import internet_tv_sim_router
from handlers.keywords import keywords_router
# from work_time.time_func import send_time_msg``


# oпределяем основную асинхронную функцию main
async def main(): 
    # scheduler.add_job(send_time_msg, 'interval', seconds=10) # добавляем задачу в планировщик scheduler
    # scheduler.start() # запускаем планировщик задач, чтобы он начал выполнять добавленные задачи по расписанию
    # добавляем роутеры в диспетчер dp
    dp.include_router(start_router) 
    dp.include_router(techsup_router)
    dp.include_router(request_router) 
    dp.include_router(internet_router) 
    dp.include_router(internet_tv_router) 
    dp.include_router(internet_sim_router) 
    dp.include_router(internet_tv_sim_router)
# запуск бота в режиме long polling при запуске бот очищает все обновления, которые были за его моменты бездействия    
    try:
        await bot.delete_webhook(drop_pending_updates=True) # пропустить накопленные апдейты
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) # запускаем бота в режиме опроса (polling).
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
