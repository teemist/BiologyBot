import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
# aiogram 100 раз обновился, будет трудно, чатгпт и дока в помощь
# https://docs.aiogram.dev/en/latest/index.html

TOKEN_API = "7415633608:AAG76hc-WY5gl8NDH1k-1qb_5dFjqac3KSU"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message()
async def echo(message: types.Message):
    await message.answer(text=message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
