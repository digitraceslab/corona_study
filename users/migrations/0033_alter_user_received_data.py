# Generated by Django 3.2 on 2021-07-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_user_has_own_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='received_data',
            field=models.BooleanField(default=False, verbose_name='Received data'),
        ),
    ]