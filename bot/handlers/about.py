from aiogram.types import Message

async def about_command(message: Message):
    await message.answer("ℹ️ CTRLZILLA_BOT – AI-базированный бот для ускорения задач и аналитики для дизайнеров и программистов.")
