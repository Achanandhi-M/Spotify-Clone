# Generated by Django 3.2.12 on 2024-04-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_alter_songmodel_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songmodel',
            name='artist',
            field=models.ManyToManyField(blank=True, to='songs.ArtistModel'),
        ),
    ]
