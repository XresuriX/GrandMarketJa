# Generated by Django 3.2.16 on 2022-12-13 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stalls', '0016_auto_20221213_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stall',
            name='owner',
        ),
    ]
