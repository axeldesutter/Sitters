# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-16 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitters', '0007_auto_20191216_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilities',
            name='Duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='disponibilities',
            name='End',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='disponibilities',
            name='Start',
            field=models.IntegerField(null=True),
        ),
    ]
