# Generated by Django 4.2.3 on 2023-07-28 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sql_db_app', '0005_remove_user_table_date_of_birth'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_table',
        ),
    ]
