# Generated by Django 3.0.8 on 2020-07-16 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0064_auto_20200716_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 16, 9, 43, 23, 971942)),
        ),
    ]
