# Generated by Django 3.2.16 on 2023-02-15 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
        ('Stalls', '0023_alter_stall_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall',
            name='category',
            field=models.ForeignKey(default='Stall', on_delete=django.db.models.deletion.CASCADE, to='catalogue.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='stall',
            name='name',
            field=models.CharField(default='MyStall', max_length=255),
        ),
        migrations.AlterField(
            model_name='stall',
            name='primary_delivery_location',
            field=models.CharField(default='kingston', max_length=150),
        ),
    ]
