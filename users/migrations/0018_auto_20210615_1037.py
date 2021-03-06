# Generated by Django 3.2 on 2021-06-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210615_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_own_device',
            field=models.BooleanField(default=False, help_text="<ul><li>Check this if you don't want us to send you a device.</li></ul>", verbose_name='I have a Polar Ignite'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, help_text="<ul><li>Address for sending the Polar sport tracker. (Don't fill if you already have one.)</li></ul>", max_length=50, verbose_name='address'),
        ),
    ]
