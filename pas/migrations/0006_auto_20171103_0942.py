# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0005_auto_20171103_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='percent',
        ),
        migrations.AddField(
            model_name='project',
            name='percent',
            field=models.IntegerField(default=0),
        ),
    ]
