import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from main import search



TOKEN = "5601906129:AAH1k-asnKub2yCS36TUmjHMUlr9UtcarW4"
dp = Dispatcher()


@dp.message(CommandStart())
async def comand_start_handler(message: Message):

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await search()

async def starts():

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(starts())
