from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Menu"))

addresses_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
addresses_keyboard.add(KeyboardButton("First"))
addresses_keyboard.add(KeyboardButton("Second"))
addresses_keyboard.add(KeyboardButton("Back"))
