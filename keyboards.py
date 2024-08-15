from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton



def genres_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Детектив"),
                KeyboardButton(text="Роман")
            ],
            [
                KeyboardButton(text="Фантастика"),
                KeyboardButton(text="Триллер")
            ]
        ],
        resize_keyboard=True
    )
    return kb

def review_rating_keyboard():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Отлично")
            ],
            [
                KeyboardButton(text="Хорошо")
            ],
        ],
        resize_keyboard=True
    )
    return kb