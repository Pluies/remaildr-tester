# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20160217_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotepoll',
            name='status',
            field=models.CharField(max_length=256),
        ),
        migrations.DeleteModel(
            name='RemotePollStatus',
        ),
    ]