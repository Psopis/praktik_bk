from tortoise import Model, fields


class User(Model):
    user_id = fields.TextField(primary_key=True)
    name = fields.TextField()
    born_date = fields.DateField(null=True)

    is_employee = fields.BooleanField(default=False)


    def __str__(self):
        return self.name, self.user_id
