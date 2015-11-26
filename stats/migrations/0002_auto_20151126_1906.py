# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='variant',
            field=models.ForeignKey(blank=True, to='stats.Variant', null=True),
        ),
    ]
