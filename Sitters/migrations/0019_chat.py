# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-17 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitters', '0018_disponibilities_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender', models.IntegerField(null=True)),
                ('Receiver', models.IntegerField(null=True)),
                ('Content', models.TextField(null=True)),
            ],
        ),
    ]