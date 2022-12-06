import logging

from aiogram import Bot, Dispatcher, executor, types
from functools import reduce
from topics import get_topics
from bot_token import API_TOKEN

FILENAMES = [
    "spiritual_and_moral_guidelines.txt",
    "family_society.txt",
    "nature_culture.txt",
]

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    logging.info(
        f"User with username @{message.from_user.username} sent start or help command. Their fullname: {message.from_user.full_name}"
    )

    await message.reply(
        "Привет! Я помогу тебе подготовиться к итоговому сочинению!\nОтправь команду /gettopics и ты получишь 6 тем из итогового сочинения 2022-2023"
    )


@dp.message_handler(commands=["gettopics"])
async def send_topics(user_message: types.Message):
    logging.info(
        f"User with username @{user_message.from_user.username} sent gettopics command. Their fullname: {user_message.from_user.full_name}"
    )

    topics = get_topics(filenames=FILENAMES)

    message = "Темы:\n\n"

    for i in range(1, 7):
        message += f"{i}) {topics[i-1]}\n"

    await user_message.reply(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
