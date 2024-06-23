from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from infrastructure.database.db_working import UserWorking
from tgbot.keyboards.inline import Profile_kb
from tgbot.keyboards.reply import main_user_profile

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await UserWorking.add_user(message.from_user.id, message.from_user.username)
    await message.reply(f"Приветсвую вас {message.from_user.username}", reply_markup=main_user_profile())


class ProfileH:
    @staticmethod
    @user_router.message(F.text == '🏡Профиль')
    async def user_main_profile(message: Message):
        user = await UserWorking.get_user(message.from_user.id)
        text = f"""     👤 *Ваш профиль* `{user.name}`\n
*Идентификатор:* `{user.user_id}`\n

📊 Ваша информация:

*День вашей регистрации:* `{user.login_date}`

*Ваша подписка:* `Нету подписки`
                        """
        await message.answer(text=text, parse_mode='Markdown', reply_markup=Profile_kb.profiles_choose_some())

    @staticmethod
    @user_router.callback_query(F.data == 'get_subscribe')
    async def back_in_main_profile(call: CallbackQuery):
        user = await UserWorking.get_user(call.from_user.id)

        await call.message.edit_text(text='💸*Выберете тарифный план:*', parse_mode='Markdown',
                                     reply_markup=Profile_kb.subscribes())

    @staticmethod
    @user_router.callback_query(F.data == 'back_in_profile')
    async def back_in_main_profile(call: CallbackQuery):
        user = await UserWorking.get_user(call.from_user.id)
        text = f"""     👤 *Ваш профиль* `{user.name}`\n
*Идентификатор:* `{user.user_id}`\n

📊 Ваша информация:

*День вашей регистрации:* `{user.login_date}`

*Ваша подписка:* `Нету подписки`
                        """
        await call.message.edit_text(text=text, parse_mode='Markdown', reply_markup=Profile_kb.profiles_choose_some())
