# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-16 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitters', '0005_auto_20191216_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponibilities',
            name='Price',
            field=models.FloatField(null=True),
        ),
    ]
