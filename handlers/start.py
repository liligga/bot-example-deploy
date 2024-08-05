from aiogram import Router, types, F
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_command_handler(message: types.Message):
    # print(vars(message.from_user))
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="Информация о нас", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Вакансии", callback_data="vacancies")
            ]
        ]
    )
    await message.answer(f"Привет, {message.from_user.first_name}, я бот Группы 44-1", reply_markup=kb)


# @start_router.callback_query(lambda callback: callback.data == "about_us")
@start_router.callback_query(F.data == "about_us")
async def aboutus_handler(callback: types.CallbackQuery):
    # await callback.answer("опвлплвповло")
    await callback.message.answer("Тут будет информация о нас")


@start_router.callback_query(F.data == "vacancies")
async def vacancies_handler(callback: types.CallbackQuery):
    # await callback.answer("опвлплвповло")
    await callback.message.answer("Тут будут вакансии")


@start_router.message(F.text == "Детектив")
async def detective_handler(message: types.Message):
    await message.answer("Книги жанра Детектив")