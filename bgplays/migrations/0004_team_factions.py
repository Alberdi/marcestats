# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgplays', '0003_auto_20151127_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='factions',
            field=models.ManyToManyField(related_name='Factions', to='bgplays.Faction'),
        ),
    ]
