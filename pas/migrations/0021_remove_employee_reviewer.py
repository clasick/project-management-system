# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0020_auto_20171105_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='reviewer',
        ),
    ]