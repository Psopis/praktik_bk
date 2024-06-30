import datetime

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, LabeledPrice

from infrastructure.database.db_working import UserWorking
from infrastructure.parsers.all_matches_parsers import parser_all_matches_flashscore
from tgbot.keyboards.inline import Profile_kb, Games_choose, start_game_and_play
from tgbot.keyboards.reply import main_user_profile, webappstart

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await UserWorking.add_user(message.from_user.id, message.from_user.username)
    await message.answer(f"Приветсвую вас {message.from_user.username}", reply_markup=main_user_profile())


class ProfileH:
    @staticmethod
    @user_router.message(F.text == '🏡Профиль')
    async def user_main_profile(message: Message):
        user = await UserWorking.get_user(message.from_user.id)
        text = f"""     👤 *Ваш профиль* `{user.name}`\n
        *Идентификатор:* `{user.user_id}`\n

        📊 Ваша информация:

        """

        if user.subscribe:
            text += f"*Последний день вашей подписки:* {user.last_day_subs}"
        else:
            text += '*Ваша подписка:* `Нету подписки`'
        await message.answer(text=text, parse_mode='Markdown', reply_markup=Profile_kb.profiles_choose_some())

    @staticmethod
    @user_router.message(F.text == '📣Выбрать матчи')
    async def user_main_profile(message: Message):

        user = await UserWorking.get_user(message.from_user.id)
        text = ''' Выберете спорт про который хотите узнать'''
        await message.answer(text=text, parse_mode='Markdown', reply_markup=Games_choose.choose_sport())

    @staticmethod
    @user_router.callback_query(F.data == 'get_subscribe')
    async def back_in_main_profile(call: CallbackQuery):
        await call.answer()
        user = await UserWorking.get_user(call.from_user.id)

        await call.message.edit_text(text='💸*Выберете тарифный план:*', parse_mode='Markdown',
                                     reply_markup=Profile_kb.subscribes())

    @staticmethod
    @user_router.callback_query(F.data == 'back_in_profile')
    async def back_in_main_profile(call: CallbackQuery):
        await call.answer()
        user = await UserWorking.get_user(call.from_user.id)
        text = f"""     👤 *Ваш профиль* `{user.name}`\n
               *Идентификатор:* `{user.user_id}`\n

               📊 Ваша информация:

               """
        if user.subscribe:
            text += f"*Последний день вашей подписки:* {user.last_day_subs}"
        else:
            text += '*Ваша подписка:* `Нету подписки`'
        await call.message.edit_text(text=text, parse_mode='Markdown', reply_markup=Profile_kb.profiles_choose_some())


class Subscribes:

    @staticmethod
    @user_router.callback_query(F.data.contains('sube_'))
    async def back_in_main_profile(call: CallbackQuery):
        await call.answer()
        data = call.data.split('_')[1]

        nums = 0
        month = 0

        if int(data) == 6:
            nums = 500
            month = 180
            p = LabeledPrice(label='Подписка на 6 месяцев', amount=50000)
        elif int(data) == 12:
            nums = 900
            month = 365
            p = LabeledPrice(label='Подписка на 12 месяцев', amount=90000)
        elif int(data) == 1:
            nums = 100
            month = 30
            p = LabeledPrice(label='Подписка на 1 месяц', amount=10000)
        text = f'''*Тариф:* на {month} дней
*Стоимость:* {nums} 🇷🇺RUB
*Срок действия:* {month} дней

*Вы получите доступ к ресурсам Телеграм бота:*

        '''
        user = await UserWorking.get_user(call.from_user.id)
        if user.subscribe:
            await call.message.answer(text="У вас уже есть подписка")
        else:
            await UserWorking.set_sub(call.from_user.id, month)
            await call.message.answer(text=text, parse_mode='Markdown')
            await call.bot.send_invoice(
                call.message.chat.id,
                title='Подписка на бота',
                description="Подписка",
                provider_token='381764678:TEST:88850',
                currency='rub',

                is_flexible=False,  # True если конечная цена зависит от способа доставки
                prices=[p],
                start_parameter='bot_',
                payload='some-invoice-payload-for-our-internal-use'
            )


class Games:

    @staticmethod
    @user_router.callback_query(F.data == 'sport_fut')
    async def back_in_main_profile(call: CallbackQuery):
        await call.answer()
        user = await UserWorking.get_user(call.from_user.id)
        arr = parser_all_matches_flashscore('f_1_0_7_ru-kz_1', 'fo_1_0_7_ru-kz_1_0')
        array = ''
        ch = 0
        array_of_games = ''
        # переделка массива чтобы проще было в js также звездочка в начале чтобы не было лишнего элемента

        for i in arr.split('*'):
            array += i + '*'
            ch += 1
            if ch == 30:
                array_of_games = array

        await call.message.answer(text='Чтобы посмотреть матчи по футболу нажмите кнопку',
                                  parse_mode='Markdown',
                                  reply_markup=start_game_and_play(str(array_of_games)))

    @staticmethod
    @user_router.callback_query(F.data == 'sport_bask')
    async def back_in_main_profile(call: CallbackQuery):
        await call.answer()
        user = await UserWorking.get_user(call.from_user.id)
        arr = parser_all_matches_flashscore('f_3_0_7_ru-kz_1', 'fo_3_0_7_ru-kz_1_0')
        array = ''
        ch = 0
        array_of_games = ''
        # переделка массива чтобы проще было в js также звездочка в начале чтобы не было лишнего элемента

        for i in arr.split('*'):
            array += i + '*'
            ch += 1
            if ch == 30:
                array_of_games = array

        await call.message.answer(text='Чтобы посмотреть матчи по баскетболу нажмите кнопку',
                                  parse_mode='Markdown',
                                  reply_markup=start_game_and_play(str(array_of_games)))

    @staticmethod
    @user_router.callback_query(F.data == 'sport_vol')
    async def back_in_main_profile(call: CallbackQuery):
        user = await UserWorking.get_user(call.from_user.id)
        arr = parser_all_matches_flashscore('f_12_0_7_ru-kz_1', 'fo_12_0_7_ru-kz_1_0')
        array = ''
        ch = 0
        array_of_games = ''
        # переделка массива чтобы проще было в js также звездочка в начале чтобы не было лишнего элемента

        for i in arr.split('*'):
            array += i + '*'
            ch += 1
            if ch == 30:
                array_of_games = array
        await call.message.answer(text='Чтобы посмотреть матчи по волейболу нажмите кнопку',
                                  parse_mode='Markdown',
                                  reply_markup=start_game_and_play(str(array_of_games)))


async def check_subs(bot):
    users = await UserWorking.get_all_users_with_subs()
    for user in users:
        print('Проверка подписки людей')
        print(user.last_day_subs)
        print(datetime.datetime.today())
        if user.last_day_subs <= datetime.datetime.today().date():
            await UserWorking.set_subscribe_false(user.user_id)
            await bot.send_message(text="У вас кончилась подписка❗❗❗\n💸Вы можете приобрести другой тариф:",
                                   reply_markup=main_user_profile(), chat_id=user.user_id)
