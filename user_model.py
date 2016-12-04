import datetime

from peewee import *

DATABASE = SqliteDatabase('user.db')

class User(Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField(max_length = 100)
    joined_at = DateTimeField(default = datetime.datetime.now)
    is_admin = BooleanField(default = False)

    class Meta:
        database = DATABASE
        """the minus sign before joined_at tells order_by to arrange by desc()."""
        order_by = ('-joined_at',)
