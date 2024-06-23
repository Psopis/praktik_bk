from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def my_orders_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(
        text="⚽Выберете матч",
        web_app=WebAppInfo('https://<your_domain>')
    )
    )
    return kb.as_markup()


class Profile_kb:
    @staticmethod
    def profiles_choose_some():
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Приобрести подписку",
            callback_data=f'get_subscribe'
        )
        )
        return kb.as_markup()

    @staticmethod
    def subscribes():
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Подписка на 1 месяц",
            callback_data=f'subscribe_'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Подписка на 6 месяцев",
            callback_data=f'subscribe_'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Подписка на 1 год",
            callback_data=f'subscribe_'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Назад",
            callback_data=f'back_in_profile'
        )
        )
        return kb.as_markup()
