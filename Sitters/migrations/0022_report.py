# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-18 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitters', '0021_user_banned'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reported', models.IntegerField(null=True)),
                ('Comment', models.TextField(null=True)),
            ],
        ),
    ]
