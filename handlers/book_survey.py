from aiogram import F, Router, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot_config import database
from keyboards import genres_keyboard


survey_router = Router()


class BookSurvey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    genre = State()


@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await message.answer("Давайте начнем опрос. Вы его можете остановить при помощи слова 'стоп'")
    await message.answer("Как Вас зовут?")


@survey_router.message(Command("stop"))
@survey_router.message(F.text == "стоп")
async def stop_survey(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос остановлен. Вы его не закончили")

@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer("Сколько Вам лет?")


@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Вводите только цифры")
        return
    age = int(age)
    if age < 12 or age > 90:
        await message.answer("Вводите числа от 12 до 90!")
        return
    await state.update_data(age=age)
    await state.set_state(BookSurvey.gender)
    await message.answer("Какого Вы пола?")


@survey_router.message(BookSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(BookSurvey.genre)
    await message.answer("Ваш любимый жанр худ литературы?", reply_markup=genres_keyboard())


@survey_router.message(BookSurvey.genre)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)

    await message.answer("Спасибо за пройденный опрос!")
    data = await state.get_data()
    print(data)

    database.execute(
        query="INSERT INTO book_survey (name, age, gender, genre) VALUES (?, ?, ?, ?)",
        params=(
            data.get('name'),
            data.get('age'),
            data.get('gender'),
            data.get('genre')
        )
    )

    # очищаем данные и состояния
    await state.clear()


