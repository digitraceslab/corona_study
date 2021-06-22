# Generated by Django 3.2 on 2021-06-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_user_device_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='received_data',
            field=models.BooleanField(default=False, verbose_name='We have received data from this subject'),
        ),
    ]