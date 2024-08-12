import asyncio
import logging

from bot_config import bot, dp, set_bot_commands, database
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.shop import shop_router
from handlers.book_survey import survey_router


async def on_startup(bot):
    print("Бот запустился")
    database.create_tables()


async def main():
    await set_bot_commands()
    # добавляем маршрутизаторы диспетчеру
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(survey_router)
    dp.include_router(shop_router)

    # в самом конце
    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
