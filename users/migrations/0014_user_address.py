# Generated by Django 3.2 on 2021-06-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210609_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='', help_text='Address for sending the Polar sport tracker.', max_length=50, verbose_name='address'),
            preserve_default=False,
        ),
    ]