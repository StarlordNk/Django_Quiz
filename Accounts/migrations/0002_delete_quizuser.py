# Generated by Django 2.2.13 on 2020-10-21 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuizUser',
        ),
    ]
