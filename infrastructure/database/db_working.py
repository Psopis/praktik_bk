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
            await User.create(user_id=user_id, name=name, is_employee=employee)

    @staticmethod
    async def get_user(user_id):
        return await User.get(user_id=user_id)


class AdminWorking:
    @staticmethod
    async def get_all_admins():
        return await User.filter(is_employee=True)

    @staticmethod
    async def add_admin(user_id, username, time):
        try:
            return await User.get(user_id=user_id)
        except tortoise.exceptions.DoesNotExist:

            await User.create(user_id=user_id, username=username, is_employee=True, date=time)

    @staticmethod
    async def check_admin(user_id):
        user = await User.get(user_id=user_id)
        return user.role_
