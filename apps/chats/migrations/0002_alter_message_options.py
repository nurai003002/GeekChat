# Generated by Django 5.0.1 on 2024-01-20 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Соощение', 'verbose_name_plural': 'Сообщения'},
        ),
    ]
