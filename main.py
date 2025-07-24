import logging
from aiogram import Bot, Dispatcher, types, executor
import openai
import os

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for bioresonance practitioners."},
            {"role": "user", "content": message.text}
        ]
    )
    await message.reply(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
