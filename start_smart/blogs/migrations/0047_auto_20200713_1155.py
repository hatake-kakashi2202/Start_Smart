# Generated by Django 3.0.8 on 2020-07-13 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0046_auto_20200712_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 13, 11, 55, 10, 565586)),
        ),
    ]