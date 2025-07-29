import asyncio
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from bot.handlers import start, help_cmd, about
from bot.handlers.ask import ask_command


load_dotenv()
TOKEN =os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Регистрируем команды
dp.message.register(start.start_command, Command("start"))
dp.message.register(help_cmd.help_command, Command("help"))
dp.message.register(about.about_command, Command("about"))
dp.message.register(ask_command, Command("ask"))


async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

def run_bot():
    asyncio.run(main())