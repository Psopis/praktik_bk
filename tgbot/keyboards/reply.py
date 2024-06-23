from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def main_user_profile() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=r'🏡Профиль')

    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)