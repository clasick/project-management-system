# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 12:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0009_auto_20171103_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.date(2018, 2, 1), verbose_name='Deadline'),
        ),
    ]
