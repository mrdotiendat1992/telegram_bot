from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import asyncio
import random

TOKEN="5800059284:AAEZW5Pa6i6GiMsmnw58f4x_dPcOz8XbI4s"

bot = Bot(TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    number = random.randint(100,999)
    await message.reply(f"Hôm nay bạn nên đánh 3 càng con: {number}")

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

