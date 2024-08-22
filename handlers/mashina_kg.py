from aiogram import Router, types
from aiogram.filters.command import Command
from crawler.mashina_kg import MashinaCrawler

mashina_router = Router()


@mashina_router.message(Command("cars"))
async def show_new_cars_handler(message: types.Message):
    crawler = MashinaCrawler()
    crawler.get_page()
    links = crawler.get_car_links()
    for link in links:
        await message.answer(link)