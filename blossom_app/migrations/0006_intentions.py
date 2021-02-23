# Generated by Django 3.1.7 on 2021-02-23 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blossom_app', '0005_auto_20210222_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intentions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intention', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intention', to='blossom_app.users')),
            ],
        ),
    ]