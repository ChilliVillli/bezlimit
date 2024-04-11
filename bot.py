import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from main import search
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext



TOKEN = "5601906129:AAH1k-asnKub2yCS36TUmjHMUlr9UtcarW4"
dp = Dispatcher()
router = Router()


class Number(StatesGroup):
    num = State()


@dp.message(CommandStart())
async def comand_start_handler(message: Message):

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@router.message(Command(commands='num'))
async def num_phone(message: Message, state: FSMContext):
    await state.set_state(Number.num)
    await message.answer("Введите номер состоящий из 10 цифр!")


@router.message(Number.num)
async def search_num(message: Message, state: FSMContext):
    await state.update_data(num=message.text)
    data = await state.get_data()
    digital_num = data['num']
    await state.clear()

    return search(digital_num)



async def starts():

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(starts())