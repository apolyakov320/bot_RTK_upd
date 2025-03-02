# импортируем необходимые модули и функции
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# клавиатура да/нет 
def yes_no_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Да', callback_data='accept')],
        [InlineKeyboardButton(text='Нет', callback_data='decline')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура личный кабинет
def lk_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Войти в личный кабинет', url ='https://b2c.passport.rt.ru/auth')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура подключить услуги
def get_services_menu_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='🌐Интернет', callback_data='internet')],
        [InlineKeyboardButton(text='🌐Интернет + 🎬ТВ', callback_data='internet_tv')],
        [InlineKeyboardButton(text='🌐Интернет + 🎬ТВ + 📱Мобильная связь', callback_data='internet_tv_sim')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура тех.проблемы
def get_techsup_menu_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='🌐Проблема с интернетом', callback_data='trouble_internet')],
        [InlineKeyboardButton(text='🎬Проблема с ТВ', callback_data='trouble_internet_tv')],
        [InlineKeyboardButton(text='❓Прочие вопросы', callback_data='trouble_other')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def techsup_buttons_1():
    inline_kb_list = [
        [InlineKeyboardButton(text='💻Чат в личном кабинете', url='https://tumen.rt.ru')],
        [InlineKeyboardButton(text='💬Написать нам в группу ВКонтакте', url='https://vk.com/rostelecom')],
        [InlineKeyboardButton(text='✍️Написать нам в Одноклассниках', url='https://ok.ru/rostelecom.official')],
        [InlineKeyboardButton(text='Назад', callback_data='techsup_back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура тарифы [Подключить услуги - Интернет]
def get_internet_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='«Технология доступа»', callback_data='get_td')],
        [InlineKeyboardButton(text='«Технология общения»', callback_data='get_to')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура подключить/к тарифам [Подключить услуги - Интернет]
def internet_rates_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Подключить', callback_data='request_user_data')],
        [InlineKeyboardButton(text='К тарифам', callback_data='internet_rates')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура тарифы [Подключить услуги - Интернет+ТВ]
def get_internet_tv_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='«Технология развлечения. Онлайн»', callback_data='get_tro')],
        [InlineKeyboardButton(text='«Технология развлечения»', callback_data='get_tr')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура подключить/к тарифам [Подключить услуги - Интернет+ТВ]
def internet_tv_rates_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Подключить', callback_data='request_user_data')],
        [InlineKeyboardButton(text='К тарифам', callback_data='internet_tv_rates')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура тарифы [Подключить услуги - Интернет+ТВ+sim]
def get_internet_tv_sim_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='«Технология выгоды»', callback_data='get_tv')],
        [InlineKeyboardButton(text='«Технология выгоды. Семья»', callback_data='get_tvs')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура подключить/к тарифам [Подключить услуги - Интернет+ТВ+sim]
def internet_tv_sim_rates_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Подключить', callback_data='request_user_data')],
        [InlineKeyboardButton(text='К тарифам', callback_data='internet_tv_sim_rates')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)





