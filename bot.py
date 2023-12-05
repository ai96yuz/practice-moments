import asyncio
import logging
import sys
# from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from constants import *


# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

print(TOKEN, type(TOKEN))


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


user_seen_facts = {}

# @dp.message(commands=['fact'])
# async def command_fact_handler(message: Message) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     user_id = message.from_user.id
#     if user_id not in user_seen_facts:
#         user_seen_facts[user_id] = []
#
#     if len(user_seen_facts[user_id]) == len(random_facts):
#         await message.answer("Ви переглянули всі доступні факти!")
#         return
#
#     unseen_facts = [fact for fact in random_facts if fact not in user_seen_facts[user_id]]
#     random_fact = random.choice(unseen_facts)
#     user_seen_facts[user_id].append(random_fact)
#
#     await message.answer(random_fact)
    # await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
# @dp.message(commands=['fact'])
# @dp.message(command_start_handler='fact')
# async def send_random_fact(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_seen_facts:
#         user_seen_facts[user_id] = []
#
#     if len(user_seen_facts[user_id]) == len(random_facts):
#         await message.answer("Ви переглянули всі доступні факти!")
#         return
#
#     # Вибір рандомного факту, який користувач ще не бачив
#     unseen_facts = [fact for fact in random_facts if fact not in user_seen_facts[user_id]]
#     random_fact = random.choice(unseen_facts)
#     user_seen_facts[user_id].append(random_fact)
#
#     await message.answer(random_fact)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
