# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-06 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgplays', '0010_game_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='virtual',
            field=models.BooleanField(default=False),
        ),
    ]
