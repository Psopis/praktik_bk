from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_game_and_play(games):
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(
        text="Играть",
        web_app=WebAppInfo(url=f"https://muko3.github.io/?games={games}")

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
            callback_data=f'sube_{1}'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Подписка на 6 месяцев",
            callback_data=f'sube_{6}'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Подписка на 1 год",
            callback_data=f'sube_{12}'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Назад",
            callback_data=f'back_in_profile'
        )
        )
        return kb.as_markup()


class Games_choose:
    @staticmethod
    def choose_sport():
        kb = InlineKeyboardBuilder()
        kb.row(InlineKeyboardButton(
            text="Футбол",
            callback_data=f'sport_fut'
        )
        )
        kb.row(InlineKeyboardButton(
            text="Баскетбол",
            callback_data=f'sport_bask'
        )
        )
        # kb.row(InlineKeyboardButton(
        #     text="Волейбол",
        #     callback_data=f'sport_vol'
        # )
        # )
        return kb.as_markup()


def test():
    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(
        text="Вчерашние матчи",
        callback_data=f"yesterday_matches"
    )
    )
    kb.row(InlineKeyboardButton(
        text="Сегодняшние матчи",
        callback_data=f'today_matches'
    )
    )
    kb.row(InlineKeyboardButton(
        text="Завтрашние матчи",
        callback_data=f'tommorow_matches'
    )
    )

    return kb.as_markup()
