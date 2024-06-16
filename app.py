import logging
import os

from db import Database
from button import menu_keyboard, addresses_keyboard

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "6997464365:AAFuIHSr1aBkUI5T2Ah0hmJCuDFwWrOg6Tw"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_2(username, full_name, user_id) VALUES('{username}', '{full_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"I am glad to see you again @{username}", reply_markup=menu_keyboard)
    else:
        await Database.connect(query, "insert")
        await message.reply(f"Hello @{username}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menu")
async def menu(message: types.Message):
    await message.answer("Menu is here >>>>>>>", reply_markup=addresses_keyboard)


@dp.message_handler(lambda message: message.text == "Back")
async def menu(message: types.Message):
    await message.answer("Back to menu >>>>>>>", reply_markup=menu_keyboard)


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
