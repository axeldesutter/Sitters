# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-18 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitters', '0022_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='By',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]