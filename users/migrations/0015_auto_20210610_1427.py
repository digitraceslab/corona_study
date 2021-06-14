# Generated by Django 3.2 on 2021-06-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(help_text='Email (aalto.fi only)', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Email (aalto.fi only)', max_length=254, unique=True, verbose_name='email address'),
        ),
    ]