# Generated by Django 3.1.7 on 2021-02-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blossom_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
