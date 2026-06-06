from aiogram import Router
from aiograms.filter import Command
srom aiogram.types import Message

router = Router()

@router.message(Command"start")
async def start(message: ):
    await message.answer("Отправь фото/фрагмента фильма\n\nНапиши /help для помощи")