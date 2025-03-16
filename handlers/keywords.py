from aiogram import types # роутер и тайпс
from create_bot import bot,dp


KEYWORDS =['ростелеком', 'интернет', 'связь', 'тв']

@dp.message()
async def handler_message(message: types.Message):
    # Проверяем, что сообщение отправлено в групповом чате
    if message.chat.type in ['group', 'supergroup']:
        # Проверяем, содержит ли сообщение ключевые слова
        if any(keyword in message.text.lower() for keyword in KEYWORDS):
            # Пересылаем сообщение администратору
            await bot.forward_message(chat_id=946891947, from_chat_id=message.chat.id, message_id=message.message_id)
            # Отправляем уведомление в чат, что сообщение переслано
            await message.reply("Сообщение переслано администратору.")