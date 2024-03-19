"""Models"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Model for users"""
    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    image = models.ImageField(upload_to='users_images', null=True, blank=True, verbose_name='avatar')

    def __str__(self):  # pylint: disable=E0307
        return self.username
