from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, WebAppInfo


class Profile_kb:
    @staticmethod
    def count__arkan(date):
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Расчитать",
            callback_data=f'arakan_{date}'
        )
        )
        return kb.as_markup()

    @staticmethod
    def main_menu():
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Сделать прогноз",
            callback_data=f'main_start_prognoz'
        )
        )
        return kb.as_markup()

class Admin_kb:
    @staticmethod
    def admins_start():
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Сделать рассылку",
            callback_data=f'send_distribution'
        )
        )
        return kb.as_markup()

    @staticmethod
    def agreement_to_send(type):
        kb = InlineKeyboardBuilder()
        kb.add(InlineKeyboardButton(
            text="Да",
            callback_data=f'agree_{type}'
        )
        )
        kb.add(InlineKeyboardButton(
            text="Нет",
            callback_data=f'disagree'
        )
        )
        return kb.as_markup()

    @staticmethod
    def agreement_to_send_replay():
        keyboard = ReplyKeyboardBuilder()
        keyboard.button(text=r'ДА')
        keyboard.button(text=r'НЕТ')
        keyboard.adjust(2)
        return keyboard.as_markup(resize_keyboard=True)
