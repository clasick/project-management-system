# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pas', '0035_auto_20171108_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pas.Team'),
        ),
    ]
