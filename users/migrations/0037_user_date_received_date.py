# Generated by Django 3.2 on 2021-09-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_alter_user_filled_surveys'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_received_date',
            field=models.DateField(default=None, null=True, verbose_name='Data received'),
        ),
    ]