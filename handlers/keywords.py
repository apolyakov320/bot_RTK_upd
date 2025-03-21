from aiogram import Router, F # роутер и "магический фильтр"
from aiogram.types import Message
from create_bot import bot, admins


keywords_router = Router()
# Хэндлер для обработки ключевых слов
@keywords_router.message(F.text.lower().contains("ростелеком") | F.text.lower().contains("интернет")| F.text.lower().contains("связь")| F.text.lower().contains("приставка")|
                         F.text.lower().contains("инет")| F.text.lower().contains("телевидение")| F.text.lower().contains("телевизор")| F.text.lower().contains("мтс")|
                         F.text.lower().contains("дом.ру")| F.text.lower().contains("билайн")| F.text.lower().contains("русская компания")| F.text.lower().contains("телесети")|
                         F.text.lower().contains("оператор")| F.text.lower().contains("провайдер")| F.text.lower().contains("ростелек")| F.text.lower().contains("телек"))
async def handle_keywords(message: Message):
        await message.answer("Мы заметили, что у вас возникла проблема. Обратитесь в техническую поддержку или ожидайте, пока с вами свяжется администратор.")
        for admin_id in admins:
            await bot.send_message(
                admin_id,
                f"⚠️ Пользователь @{message.from_user.username} (ID: {message.from_user.id}) написал сообщение с ключевым словом:\n\n"
                f"<b>Текст сообщения:</b>\n{message.text}",
                parse_mode="HTML"
            )