# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20171117_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='profile_photo',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
