import datetime
import time
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, LabeledPrice

from infrastructure.database.db_working import UserWorking, AdminWorking

from tgbot.keyboards.inline import Profile_kb, Admin_kb


def count_arkan(date):
    day = date.split('.')[0]
    month = date.split('.')[1]
    year = date.split('.')[2]
    new_day = 0
    new_year = 0
    if int(day) >= 23:
        new_day = int(day) - 22
    else:
        new_day = int(day)
    count_year = list(year)
    for i in count_year:
        new_year = int(i) + new_year
    if new_year >= 23:
        new_year = int(new_year) - 22
    else:
        new_year = int(new_year)
    position_five = new_year + int(month)
    position_seven = new_day + position_five
    return new_day, int(month), new_year, position_five, position_seven


user_router = Router()


class Dates(StatesGroup):
    date = State()
    start_arkan = State()


@user_router.message(CommandStart())
async def user_start(message: Message, state: FSMContext):
    if message.from_user.id == 6998895854:
        await AdminWorking.add_admin(message.from_user.id, message.from_user.username)
        await message.answer(
            f"Приветсвую вас админ {message.from_user.username}.", reply_markup=Admin_kb.admins_start()
        )
    else:
        await UserWorking.add_user(message.from_user.id, message.from_user.username)
        await message.answer(text=f"Приветсвую вас {message.from_user.username}.",
                             reply_markup=Profile_kb.main_menu()

                             )


class ProfileH:
    @staticmethod
    @user_router.callback_query(F.data.contains('main_start_prognoz'))
    async def choosing_neuro_to_txtimg(call: CallbackQuery, state: FSMContext):
        await call.answer()
        await call.message.edit_text(text='Напишите свою дату рождения в формате дд.мм.гггг')
        await state.set_state(Dates.date)

    @staticmethod
    @user_router.message(Dates.date)
    async def user_main_profile(message: Message, state: FSMContext):

        print(message.text)
        try:
            arkan = count_arkan(message.text)
            valid_date = time.strptime(message.text, '%d.%m.%Y')
            await message.answer(text=f'Расчет на дату {message.text}\nПозиция 1: {arkan[0]}\n'
                                      f'Позиция 2: {arkan[1]}\n'
                                      f'Позиция 3: {arkan[2]}\n'
                                      f'Позиция 5: {arkan[3]}\n'
                                      f'Позиция 7: {arkan[4]}\n'
                                 )
            await UserWorking.set_born_date(message.from_user.id, message.text)


        except ValueError:
            await message.edit_text(
                text="Произошла ошибка при выполнении расчетов. Пожалуйста, введите дату в формате 'ДД.ММ.ГГГГ'.")
            await state.set_state(Dates.date)
        await message.answer(text=f"Приветсвую вас {message.from_user.username}.",
                             reply_markup=Profile_kb.main_menu())
