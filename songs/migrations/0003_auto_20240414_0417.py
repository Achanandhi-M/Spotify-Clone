# Generated by Django 3.2.12 on 2024-04-14 04:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0002_auto_20240413_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='songmodel',
            name='thumbnail',
            field=models.ImageField(default='default/user.png', upload_to='song_thumbnails/'),
        ),
        migrations.AlterField(
            model_name='artistmodel',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
