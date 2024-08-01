import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging


load_dotenv()
token = getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command_handler(message: types.Message):
    # print(vars(message.from_user))
    await message.answer(f"Привет, {message.from_user.first_name}, я бот Группы 44-1")


@dp.message(Command("picture"))
async def picture_handler(message: types.Message):
    image = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(
        photo=image,
        caption="Крутой кот"
    )
    await message.reply_photo(
        photo=image,
        caption="Крутой кот"
    )


@dp.message()
async def echo_handler(message: types.Message):
    await message.reply(message.text)


async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
