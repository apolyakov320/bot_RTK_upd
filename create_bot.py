# Импортируем необходимые библиотеки и модули
import logging # логирование для записи событий и ошибок в процессе работы бота
from aiogram import Bot, Dispatcher # классы бот и диспетчер для создания и управления ботом
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage # импортируем класс MemoryStorage для хранения состояний конечного автомата (FSM) в памяти
from decouple import config # импортируем функцию config из библиотеки python-decouple для загрузки переменных окружения из файла .env
from apscheduler.schedulers.asyncio import AsyncIOScheduler # импортируем класс AsyncIOScheduler из библиотеки APScheduler для планирования задач 

# Создаем объект для работы с базой данных PostgreSQL
'''from db_handler.db_class import PostgresHandler

pg_db = PostgresHandler(config('PG_LINK'))'''
# Создаем планировщик задач
scheduler = AsyncIOScheduler(timezone='Asia/Yekaterinburg')
# Настраиваем список админов
admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]
# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Инициализируем бота и диспетчера
bot = Bot(token=config('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())