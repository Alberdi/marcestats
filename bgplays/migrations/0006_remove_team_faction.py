# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgplays', '0005_auto_20160112_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='faction',
        ),
    ]
