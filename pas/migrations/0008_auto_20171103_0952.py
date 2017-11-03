# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 09:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0007_auto_20171103_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='duration',
        ),
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
