from aiogram.types import Message

async def help_command(message: Message):
    await message.answer("🛠 Команды:\n/start – запуск бота\n/help – помощь\n/about – о проекте")
