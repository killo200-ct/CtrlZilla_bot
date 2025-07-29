import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8040200513:AAFvdb3hV-I-T-enBW-zWecS-5F5roYYnyM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я 1win WorkHelper AI Bot 🚀")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
