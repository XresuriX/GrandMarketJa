# Generated by Django 3.2.16 on 2023-03-12 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partner', '0007_alter_partner_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='manager',
            field=models.OneToOneField(default='customer.CustomUser', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]