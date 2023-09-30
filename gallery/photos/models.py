
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='images', verbose_name='Фото', default='images/blank.jpg')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    author = models.ForeignKey(verbose_name='автор', to=get_user_model(), on_delete=models.CASCADE, related_name='photos')
    likers = models.ManyToManyField(verbose_name='лайки пользователей', blank=True, to=get_user_model(), related_name="favorites")

    def __str__(self):
        return self.description