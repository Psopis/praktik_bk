from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, InputFile, ReplyKeyboardRemove

from infrastructure.database.db_working import UserWorking

from tgbot.keyboards.inline import Admin_kb

admin_router = Router()


class TextState(StatesGroup):
    text = State()
    photo_send = State()
    text_send = State()


class AdminsH:
    @staticmethod
    @admin_router.callback_query(F.data.contains('send_distribution'))
    async def choosing_neuro_to_txtimg(call: CallbackQuery, state: FSMContext):
        await call.answer()
        await call.message.answer(text='Напишите текст который хотите отправить')
        await state.set_state(TextState.text)

    @staticmethod
    @admin_router.message(TextState.text)
    async def text_set(message: Message, state: FSMContext):

        if message.photo:

            await message.answer_photo(caption=f'Напишите ДА и текст отправится\n\n {message.caption}',
                                       reply_markup=Admin_kb.agreement_to_send_replay(),
                                       photo=message.photo[-1].file_id)
            await state.update_data(caption=message.caption)
            await state.update_data(photo=message.photo[-1].file_id)
            await state.set_state(TextState.photo_send)
        else:

            await message.answer(text=f'Напишите ДА и текст отправится \n\n, {message.text}',
                                 reply_markup=Admin_kb.agreement_to_send_replay(),
                                 )
            await state.update_data(text=message.text)
            await state.set_state(TextState.text_send)

    # @staticmethod
    # @admin_router.callback_query(F.data.contains('disagree'))
    # async def choosing_neuro_to_txtimg(call: CallbackQuery, state: FSMContext):
    #     await call.answer()
    #     await state.clear()
    #     await call.message.answer(text='Вы отменили отправку')
    #     await call.message.answer(
    #         f"Здравствуйте {call.from_user.username}.", reply_markup=Admin_kb.admins_start()
    #     )
    #
    # @staticmethod
    # @admin_router.callback_query(F.data.contains('agree_'))
    # async def choosing_neuro_to_txtimg(call: CallbackQuery, state: FSMContext):
    #     await call.answer()
    #     data_type = call.data.split('_')[1]
    #     print(data_type)
    #     if data_type == 'text':
    #         print(1)
    #         await call.message.answer(text='Для подтверждения нажмите или напишите ДА а для отказа НЕТ',
    #                                   reply_markup=Admin_kb.agreement_to_send_replay())
    #
    #
    #
    #     else:
    #         print(2)
    #         await call.message.answer(text='Для подтверждения нажмите или напишите ДА а для отказа НЕТ',
    #                                   reply_markup=Admin_kb.agreement_to_send_replay())
    #
    #
    # @staticmethod
    # @admin_router.message(F.text == "НЕТ")
    # async def choosing_neuro_to_txtimg(message: Message, state: FSMContext):
    #     await message.answer(text='Cообщение не отправлено', reply_markup=ReplyKeyboardRemove())
    #
    #     await state.clear()
    #     await message.answer(text='Вы отменили отправку')
    #     await message.answer(
    #         f"Здравствуйте {message.from_user.username}.", reply_markup=Admin_kb.admins_start()
    #     )
    #
    # @staticmethod
    # @admin_router.message(F.text == "ДА")
    # async def choosing_neuro_to_txtimg(message: Message, state: FSMContext):
    #     await message.answer(text='Cообщение  отправлено', reply_markup=ReplyKeyboardRemove())
    #
    #     await message.answer(
    #         f"Здравствуйте {message.from_user.username}.", reply_markup=Admin_kb.admins_start()
    #     )

    @staticmethod
    @admin_router.message(TextState.text_send)
    async def uadmon_sendo(message: Message, state: FSMContext):
        data = await state.get_data()
        print(message.text)
        if message.text == 'ДА':

            all_users = await UserWorking.get_all_user_id()
            for user in all_users:
                await message.bot.send_message(text=data.get('text'), chat_id=user.user_id)
            await state.clear()
        else:
            await message.answer(text='Текст не был отправлен')

    @staticmethod
    @admin_router.message(TextState.photo_send)
    async def uadmon_sendo(message: Message, state: FSMContext):
        data = await state.get_data()
        print(message.text)
        if message.text == 'ДА':
            all_users = await UserWorking.get_all_user_id()
            for user in all_users:
                await message.bot.send_photo(caption=data.get('caption'), photo=data.get('photo'), chat_id=user.user_id)
            await state.clear()
        else:
            await message.answer(text='Текст не был отправлен')
