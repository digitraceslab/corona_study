# Generated by Django 3.2 on 2021-06-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20210621_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_received_email',
            field=models.BooleanField(default=False, verbose_name='Has received email'),
        ),
    ]
