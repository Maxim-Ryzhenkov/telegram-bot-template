import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
# В этом примере предполагается, что он храниться локально в переменной окружения LIBRATIO_BOT
BOT_TOKEN = os.getenv("LIBRATIO_BOT")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет! Я эхо-бот!\nНапиши мне что-нибудь, а я повторю твое сообщение.')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь.\nВ ответ я пришлю тебе твое сообщение.\n Больше я ничего не умею.'
    )


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print("Принята фотография!")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_photo(message.photo[0].file_id)


# Этот хэндлер будет срабатывать на отправку боту аудиофайла
async def send_audio_echo(message: Message):
    print("Принят аудиофайл")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer_audio(message.audio.file_id)


# Этот хэндлер будет срабатывать на отправку боту голосового сообщения
async def send_voice_echo(message: Message):
    print("Принято голосовое сообщение!")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer(text="Получена голосовуха от вас. Вот она.")
    await message.reply_voice(message.voice.file_id)


# Этот хэндлер будет срабатывать на отправку боту видео-сообщения
async def send_video_echo(message: Message):
    print("Принято видео!")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_video(message.video.file_id)

# Можно добавить хэндлеры для остальных типов медиаконтента.
# await message.answer_sticker(message.sticker.file_id)
# await message.answer_animation(message.animation.file_id)
# Document


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_text_echo(message: Message):
    print("Принято текстовое сообщение!")
    # Выведет в консоль структуру апдейта.
    # Нужно только для отладки и удовлетворения любопытства.
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply(text=message.text)


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    try:
        print("Принят апдейт не пойманный ни одним обработчиком!")
        # Выведет в консоль структуру апдейта.
        # Нужно только для отладки и удовлетворения любопытства.
        print(message.model_dump_json(indent=4, exclude_none=True))
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.foto)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_text_echo)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
