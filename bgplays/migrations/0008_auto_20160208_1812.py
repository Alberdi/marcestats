# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgplays', '0007_auto_20160112_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='comments',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='factions',
            field=models.ManyToManyField(to='bgplays.Faction', blank=True),
        ),
    ]
