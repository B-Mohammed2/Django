# Generated by Django 4.2.3 on 2023-08-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0015_comments_and_feedback_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_table',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]