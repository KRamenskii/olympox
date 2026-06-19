from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    middle_name = models.CharField(
        'Отчество',
        max_length=150,
        blank=True
    )

    photo = models.ImageField(
        'Фото',
        upload_to='users/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self):
        return (
            f'{self.last_name} '
            f'{self.first_name} '
            f'{self.middle_name}'
        ).strip()

    def __str__(self):
        return self.full_name or self.username