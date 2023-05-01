from django.db import models
from django.contrib.auth.models import User

USER_TYPE = (
    ('Админ', 'Aдмин'),
    ('VIP Клиент', "VIP Клиент"),
    ('Клиент', 'Клиент')
)

GENDER = (
    ('M', "M"),
    ('Ж', 'Ж')
)
class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    user_type = models.CharField(max_length=100, choices=USER_TYPE, verbose_name='Тип пользователя')
    phone_number = models.CharField(verbose_name='Номер телефона', null=True, max_length=100)
    age = models.PositiveIntegerField('Возраст')
    gender = models.CharField(max_length=100, choices=GENDER)

