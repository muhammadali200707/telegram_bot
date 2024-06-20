import logging
from db import Database
from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_keyboard, menu_detail, mahsulot_button
from inline_button import keyboard
import asyncio

API_TOKEN = "7450181024:AAHK4U9bJ5Pcbib3GoluxgHdo2uu87ieL08"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    ful_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_2 (username, full_name, user_id) VALUES ('{username}', '{ful_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Assalomu aleykum sizni ko'rganimdan xursantman  {ful_name}", reply_markup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Xushkelibsiz {ful_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("1 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=menu_detail)


@dp.message_handler(lambda message: message.text == "Menyu 2")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:")


@dp.message_handler(lambda message: message.text == "Back")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Menyulardan birini tanglang:", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Mahsulot 1")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2 - bo'lim. Mahsulotlardan birini tanglang:", reply_markup=mahsulot_button)


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    if message.from_user.id in [6103459824, 1001968950]:
        await message.reply("Salom admin")
        photo_path = "telegram_bot/img.png"
        await bot.send_photo(message.chat.id, photo=photo_path)
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
