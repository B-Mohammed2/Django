# Generated by Django 4.2.3 on 2023-07-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sql_db_app', '0008_delete_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(default='000-0000-000000', max_length=15)),
            ],
        ),
    ]
