# Generated by Django 2.1.5 on 2020-07-13 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200711_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 12, 10, 38, 476108)),
        ),
    ]
