# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(default='ANON', max_length=20),
        ),
    ]