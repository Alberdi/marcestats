# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgplays', '0002_auto_20151126_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='faction',
            field=models.ForeignKey(blank=True, to='bgplays.Faction', null=True),
        ),
    ]
