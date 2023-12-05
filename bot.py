import asyncio
import logging
import sys
import random
import os
import aiofiles

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InputFile
from aiogram.utils.markdown import hbold
from aiogram.filters import Command

from pytube import YouTube

from constants import TOKEN, random_facts, useful_tips

bot = Bot(TOKEN)
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


# async def download_video(video_link):
#     try:
#         yt = YouTube(video_link)
#         video_path = f'{os.path.expanduser("~")}/Downloads/{yt.title}.mp4'
#         print(video_path)
#         video = yt.streams.filter(progressive=True, file_extension='mp4').first()
#         video.download(video_path)
#         return "Video downloaded successfully!"
#     except Exception as e:
#         return f"Error: {e}"
#
#
# @dp.message(Command(commands=['download']))
# async def download_command(message: types.Message):
#     video_url = message.text.split(maxsplit=1)[1]
#     video_path = await download_video(video_url)
#
#     if video_path:
#         video = types.InputFile(video_path)
#         await message.reply_video(video)
#         await aiofiles.os.remove(video_path)
#     else:
#         await message.reply("Video was not downloaded properly.")
async def download_video(video_link):
    try:
        yt = YouTube(video_link)
        video_path = f'{os.path.expanduser("~")}/Downloads/{yt.title}.mp4'
        print(video_path)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download(video_path)
        return video_path
    except Exception as e:
        print(f"Error: {e}")
        return None


@dp.message(Command(commands=['download']))
async def download_command(message: types.Message):
    video_url = message.text.split(maxsplit=1)[1]
    video_path = await download_video(video_url)

    if video_path and os.path.isfile(video_path):
        await message.reply("Video downloaded. Sending back to you...")
        with open(video_path, 'rb') as video_file:
            video = video_file.read()
            await bot.send_video(message.chat.id, video)

        os.remove(video_path)
    else:
        await message.reply("Video was not downloaded properly.")


# ////// end
async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
