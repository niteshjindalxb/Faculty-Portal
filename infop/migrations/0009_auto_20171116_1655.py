# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infop', '0008_auto_20171116_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='p_photo',
            field=models.FileField(blank=True, default='12.jpg', null=True, upload_to=''),
        ),
    ]
