# Generated by Django 3.2.3 on 2021-05-26 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210526_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
    ]
