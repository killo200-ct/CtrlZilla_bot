import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def ask_gpt(prompt: str) -> str:
    """Отправляем запрос к GPT-4o-mini (новый OpenAI SDK)."""
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты полезный ассистент для дизайнеров и программистов 1win."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Ошибка запроса к OpenAI: {e}"
