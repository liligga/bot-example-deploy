from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from database.database import Database


load_dotenv()
database = Database("db.sqlite3")

# token = getenv("BOT_TOKEN")
# bot = Bot(token=token)
# dp = Dispatcher()

dev = getenv("DEV", 0)
if not dev:
    from aiogram.client.session.aiohttp import AiohttpSession

    print("started on server")
    print(getenv("BOT_TOKEN"))
    session = AiohttpSession(proxy=getenv("PROXY"))
    bot = Bot(token=getenv("BOT_TOKEN"), session=session)

else:
    print("started on dev")
    bot = Bot(token=getenv("BOT_TOKEN"))


dp = Dispatcher()


async def set_bot_commands():
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Начало"),
            types.BotCommand(
                command="picture", description="Получите картику"
            ),
            types.BotCommand(command="shop", description="Наш каталог книг"),
        ]
    )
