from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import GalleryUserManager


# Create your models here.
class GalleryUser(AbstractUser):
    first_name = None
    last_name = None
    email = None

    username = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар',
        default='user_pic/blank.jpg'
    )

    objects = GalleryUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []