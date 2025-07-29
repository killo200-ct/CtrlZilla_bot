from aiogram.types import Message
from bot.utils.ai import ask_gpt

async def ask_command(message: Message):
    user_prompt = message.text.replace("/ask", "").strip()
    if not user_prompt:
        await message.answer("Напиши вопрос после команды /ask")
        return
    reply = await ask_gpt(user_prompt)
    await message.answer(reply)
