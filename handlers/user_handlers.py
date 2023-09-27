from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from lexicon.lexicon_ru import LEXICON_RU


router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=ReplyKeyboardRemove())


@router.message(F.text == "какой-то текст...")
async def process_no_answer(message: Message):
    await message.answer(text="какой-то ответ...")

