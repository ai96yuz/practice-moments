import asyncio
import logging
import sys
import random

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.filters import Command

from constants import TOKEN, random_facts, useful_tips

dp = Dispatcher()
user_seen_facts = {}


@dp.message(Command(commands='start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command(commands='fact'))
async def command_fact_handler(message: Message) -> None:
    user_id = message.from_user.id
    if user_id not in user_seen_facts:
        user_seen_facts[user_id] = []

    if len(user_seen_facts[user_id]) == len(random_facts):
        await message.answer("You've seen all available facts!")
        return

    unseen_facts = [fact for fact in random_facts if fact not in user_seen_facts[user_id]]
    random_fact = random.choice(unseen_facts)
    user_seen_facts[user_id].append(random_fact)

    await message.answer(random_fact)


@dp.message(Command(commands='tips'))
async def command_tips_handler(message: Message) -> None:
    random_tip = random.choice(useful_tips)
    await message.answer(random_tip)


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
