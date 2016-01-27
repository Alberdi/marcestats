# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgplays', '0006_remove_team_faction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='factions',
            field=models.ManyToManyField(to='bgplays.Faction'),
        ),
    ]
