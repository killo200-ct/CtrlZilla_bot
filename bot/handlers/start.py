from aiogram.types import Message

async def start_command(message: Message):
    await message.answer("👋 Привет! Я CTRLZILLA_BOT – твой AI-ассистент для 1win.")
