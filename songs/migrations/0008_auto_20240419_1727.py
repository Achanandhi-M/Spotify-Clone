# Generated by Django 3.2.12 on 2024-04-19 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_auto_20240414_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='movie_thumbnails')),
                ('director', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.artistmodel')),
            ],
        ),
        migrations.AddField(
            model_name='songmodel',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.moviesmodel'),
        ),
    ]
