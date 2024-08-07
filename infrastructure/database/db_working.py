import datetime

import tortoise

from infrastructure.database.models import User


class UserWorking:
    @staticmethod
    async def add_user(user_id, name, employee=False):
        try:
            print(1)
            return await User.get(user_id=user_id)
        except tortoise.exceptions.DoesNotExist:
            print(2)
            await User.create(user_id=user_id, name=name, is_employee=employee
                              )

    @staticmethod
    async def get_user(user_id):
        return await User.get(user_id=user_id)

    @staticmethod
    async def set_born_date(user_id, date):
        user = await User.get(user_id=user_id)

        user.date = date
        await user.save()

    @staticmethod
    async def get_all_user_id():
        return await User.all()


class AdminWorking:
    @staticmethod
    async def get_all_admins():
        return await User.filter(is_employee=True)

    @staticmethod
    async def add_admin(user_id, username):
        try:
            return await User.get(user_id=user_id)
        except tortoise.exceptions.DoesNotExist:

            await User.create(user_id=user_id, name=username, is_employee=True)
