# Generated by Django 3.2.16 on 2023-03-13 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0008_alter_partner_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='manager',
        ),
    ]