from tortoise import Model, fields


class User(Model):
    user_id = fields.TextField(primary_key=True)
    name = fields.TextField()
    last_day_subs = fields.DateField(null=True)
    subscribe = fields.BooleanField(default=False)
    is_employee = fields.BooleanField(default=False)


    def __str__(self):
        return self.name, self.user_id
