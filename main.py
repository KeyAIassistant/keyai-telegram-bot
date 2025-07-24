
from aiogram import Bot, Dispatcher, types
from aiogram.runner import run_polling
import os
import asyncio

# Load token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Sample handler
@dp.message()
async def handle_message(message: types.Message):
    await message.answer("Hello from KeyAI bot!")

# Run the bot
if __name__ == "__main__":
    asyncio.run(run_polling(dp))
