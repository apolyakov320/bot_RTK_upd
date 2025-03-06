# импортируем необходимые модули и функции
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_kb():
   inline_kb_list = [
        [InlineKeyboardButton(text='🚀 Подключить услуги', callback_data='connect_services')],
        [InlineKeyboardButton(text='🛠️ Тех.поддержка', callback_data='techsup')],
        [InlineKeyboardButton(text='📦 Переезд', callback_data='relocation')]
    ]
   return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура [Подключить услуги]
def get_services_menu_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='🌐Интернет', callback_data='internet')],
         [InlineKeyboardButton(text='🌐Интернет + 🎬ТВ', callback_data='internet_tv')],
        [InlineKeyboardButton(text='🌐Интернет + 📱SIM-карта', callback_data='internet_sim')],
        [InlineKeyboardButton(text='🌐Интернет + 🎬ТВ + 📱SIM-карта', callback_data='internet_tv_sim')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура тарифы [Подключить услуги - Интернет]
def internet_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Оставить заявку', callback_data='request_user_data')],
        [InlineKeyboardButton(text='Добавить услугу ТВ', callback_data='need_tv')],
        [InlineKeyboardButton(text='Добавить услугу Sim-карта', callback_data='need_sim')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_services')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура тарифы [Подключить услуги - Интернет+ТВ]
def internet_tv_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Оставить заявку', callback_data='request_user_data')],
        [InlineKeyboardButton(text='Добавить услугу Sim-карта', callback_data='need_tv_sim')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_services')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура тарифы [Подключить услуги - Интернет+Sim]
def internet_sim_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Оставить заявку', callback_data='request_user_data')],
        [InlineKeyboardButton(text='Добавить услугу ТВ', callback_data='need_tv_sim')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_services')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура тарифы [Подключить услуги - Интернет+ТВ+sim]
def internet_tv_sim_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Оставить заявку', callback_data='request_user_data')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_services')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура Тех.поддержка
def get_techsup_menu_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='🌐Проблема с интернетом', callback_data='trouble_internet')],
        [InlineKeyboardButton(text='🎬Проблема с ТВ', callback_data='trouble_internet_tv')],
        [InlineKeyboardButton(text='❓Прочие вопросы', callback_data='trouble_other')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура [Тех.поддержка - Личный кабинет]
def get_techsup_lk_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='💻Личный кабинет Сайт', url ='https://b2c.passport.rt.ru/auth')],
        [InlineKeyboardButton(text='🤖Личный кабинет Android', url ='https://play.google.com/store/apps/details?id=com.dartit.RTcabinet&hl=ru&pli=1')],
        [InlineKeyboardButton(text='🍏Личный кабинет IOS', url ='https://apps.apple.com/ru/app/%D0%BC%D0%BE%D0%B9-%D1%80%D0%BE%D1%81%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC/id561082205')],
        [InlineKeyboardButton(text='Назад', callback_data='techsup_back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def techsup_social_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='💬Написать нам ВКонтакте', url ='https://vk.com/im?entrypoint=community_page&media=&sel=-24720111')],
        [InlineKeyboardButton(text='✍️Написать нам в Одноклассниках ', url ='https://ok.ru/dk?st.cmd=anonymMain&st.lgi=HbNDWWF9V4nT')],
        [InlineKeyboardButton(text='Назад', callback_data='techsup_back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# ввести номер/назад
def enter_number_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Ввести номер', callback_data='enter_number')],
        [InlineKeyboardButton(text='Назад', callback_data='techsup_back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

# клавиатура да/нет 
def yes_no_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Да', callback_data='accept')],
        [InlineKeyboardButton(text='Нет', callback_data='decline')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)