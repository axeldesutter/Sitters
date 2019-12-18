# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-17 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitters', '0012_message_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sitter', models.IntegerField(null=True)),
                ('Parent', models.IntegerField(null=True)),
                ('Reservation', models.IntegerField(null=True)),
                ('Note', models.IntegerField(null=True)),
                ('Comment', models.TextField(null=True)),
                ('Answer', models.BooleanField(default=False)),
                ('Related', models.IntegerField(null=True)),
            ],
        ),
    ]