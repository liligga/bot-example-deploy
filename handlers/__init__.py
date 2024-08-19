from aiogram import F, Router

from .shop import shop_router
from .echo import echo_router
from .book_survey import survey_router
from .start import start_router
from .picture import picture_router
from .group_activities import group_router

private_router = Router()

private_router.include_router(survey_router)
private_router.include_router(start_router)
private_router.include_router(picture_router)
private_router.include_router(shop_router)
private_router.include_router(echo_router)

private_router.message.filter(F.chat.type == "private")