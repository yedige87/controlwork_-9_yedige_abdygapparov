# Generated by Django 4.2.5 on 2023-09-30 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='images/blank.jpg', null=True, upload_to='images', verbose_name='Фото')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Подпись')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('likers', models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL, verbose_name='лайки пользователей')),
            ],
        ),
    ]