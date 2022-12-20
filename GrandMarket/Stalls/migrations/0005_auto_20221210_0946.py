# Generated by Django 3.2.16 on 2022-12-10 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Stalls', '0004_auto_20221205_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='stall',
            name='code',
            field=oscar.models.fields.autoslugfield.AutoSlugField(blank=True, default=models.CharField(blank=True, max_length=255, null=True), editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='stallstock',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customuser', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='stallstock',
            name='price_currency',
            field=models.CharField(default='JMD', max_length=12, verbose_name='Currency'),
        ),
    ]
