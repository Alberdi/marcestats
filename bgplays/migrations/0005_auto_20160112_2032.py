# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def make_many_factions(apps, schema_editor):
	Team = apps.get_model('bgplays', 'Team')

	for team in Team.objects.all():
		if team.faction:
			team.factions.add(team.faction)


class Migration(migrations.Migration):

    dependencies = [
        ('bgplays', '0004_team_factions'),
    ]

    operations = [
			migrations.RunPython(make_many_factions)
    ]
