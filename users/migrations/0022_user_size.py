# Generated by Django 3.2 on 2021-06-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20210617_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='size',
            field=models.CharField(choices=[('S', '130–185 mm'), ('M/L', '155–210 mm')], default='M/L', max_length=9),
            preserve_default=False,
        ),
    ]