# Generated by Django 3.2.16 on 2022-12-13 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stalls', '0019_alter_stall_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall',
            name='image',
            field=models.ImageField(default='download.png', max_length=200, null=True, upload_to='oscar/images/stall_img'),
        ),
    ]
