import asyncio
import random
import string
import keyboards

import emoji
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import TOKEN_API

# aiogram 100 раз обновился, будет трудно, чатгпт и дока в помощь
# https://docs.aiogram.dev/en/latest/index.html

HELP = """
/help - список команд
/start - старт бота
/random - рандомная буква алфавита
/count - счетчик вызовов текущей команды
/description - описание бота
/sticker - вывод стикера
/give - еще один стикер
/hello - стикер вишни в лс
/picture - картинка в лс
В ответ на hello бот отправит картинку
"""

counter = 0

bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot)


async def on_startup(_):
    print('Старт работы бота')


@dp.message(Command('inline'))
async def show_inline_kb(message: types.Message):
    await bot.send_message(message.from_user.id, text="Открываю inline клавиатуру...", reply_markup=keyboards.ikb)


# Простейшие методы для обработки вводимых команд
@dp.message(Command('start'))
async def help_answer(message: types.Message):
    await message.answer("Привет, я тг бот")
    await message.delete()
    await bot.send_message(message.from_user.id, text="Открываю клавиатуру...", reply_markup=keyboards.kb)


@dp.message(Command('help'))
async def help_answer(message: types.Message):
    await message.answer(HELP)
    await message.delete()


@dp.message(Command('random'))
async def help_answer(message: types.Message):
    await message.answer(random.choice(string.ascii_letters))
    await message.delete()


@dp.message(Command('description'))
async def help_answer(message: types.Message):
    await message.answer("Привет, я тг бот и я умею выводить рандомную букву алфавита")
    await message.delete()


@dp.message(Command('count'))
async def help_answer(message: types.Message):
    global counter
    counter += 1
    await message.answer(f"Вы вызывали эту команду {counter} раз")
    await message.delete()


@dp.message(Command('sticker'))
async def send_sticker(message: types.Message):
    await message.delete()
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEM0U1m6E5_iGMgECM6YcV1O5TvEWTIIAAC1AgAAvoLtgh-i7fMmjbHJzYE")


@dp.message(Command('give'))
async def send_sticker(message: types.Message):
    await message.delete()
    await message.answer("Смотри какой я ленивый :thumbs_up:")
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEM0U1m6E5_iGMgECM6YcV1O5TvEWTIIAAC1AgAAvoLtgh-i7fMmjbHJzYE")


@dp.message(Command('picture'))
async def send_pic(message: types.Message):
    await message.delete()
    await bot.send_photo(message.from_user.id, photo="https://ir-5.ozone.ru/s3/multimedia-1-k/wc1000/7029640172.jpg")


# Обработка сообщения с текстом "hello"
@dp.message()
async def hello(message: types.Message):
    if message.text.lower() == "hello":
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAEM0f1m6RpljjHk7Gd9bU7v4uVIoS-d5gACFQADwDZPE81WpjthnmTnNgQ")


async def main():
    await dp.start_polling(bot, skip_updates=True)


# Если есть 0 в тексте сообщения - бот отправит YES, если нет - вернет сообщение
@dp.message()
async def echo(message: types.Message):
    if '0' in message.text:
        await message.answer("YES")
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    asyncio.run(main())
