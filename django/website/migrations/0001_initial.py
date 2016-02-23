# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemotePoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(verbose_name='date started at')),
                ('completed_at', models.DateTimeField(verbose_name='date completed at')),
            ],
        ),
        migrations.CreateModel(
            name='RemotePollStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='remotepoll',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.RemotePollStatus'),
        ),
    ]