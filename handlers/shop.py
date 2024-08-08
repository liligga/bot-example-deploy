from aiogram import F, Router, types
from aiogram.filters.command import Command


shop_router = Router()


@shop_router.message(Command("shop"))
async def shop_command_handler(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Детектив"),
                types.KeyboardButton(text="Роман")
            ],
            [
                types.KeyboardButton(text="Фентези"),
                types.KeyboardButton(text="Триллер")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите жанр книг", reply_markup=kb)


@shop_router.message(F.text.lower() == "детектив")
async def detective_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Книги жанра Детектив", reply_markup=kb)


@shop_router.message(F.text.lower() == "роман")
async def detective_handler(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Книги жанра Роман", reply_markup=kb)