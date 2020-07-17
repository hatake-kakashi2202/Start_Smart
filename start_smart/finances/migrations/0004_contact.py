# Generated by Django 3.0.8 on 2020-07-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_finances_transactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=13)),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('waiting', 'WAITING'), ('closed', 'CLOSED')], default='open', max_length=20)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
