# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 12:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20171119_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 19, 17, 58, 56, 515740)),
        ),
    ]
