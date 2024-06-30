from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, WebAppInfo


def main_user_profile() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=r'🏡Профиль')
    keyboard.button(text=r'📣Выбрать матчи')
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)


def webappstart() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text=r'📣Выбрать матчи', web_app=WebAppInfo('https://muko3.github.io/'))
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)
