# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 22:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remotepollstatus',
            old_name='status',
            new_name='label',
        ),
    ]