# Generated by Django 3.2 on 2021-06-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210602_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='privacy',
            field=models.BooleanField(default=False, verbose_name='consent'),
        ),
        migrations.AlterField(
            model_name='user',
            name='consent',
            field=models.BooleanField(default=False, verbose_name='consent'),
        ),
    ]
