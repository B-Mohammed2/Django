# Generated by Django 4.2.3 on 2023-07-28 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sql_db_app', '0009_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_table',
            name='phone_number',
        ),
    ]