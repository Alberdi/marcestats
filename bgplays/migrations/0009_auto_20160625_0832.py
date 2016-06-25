# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgplays', '0008_auto_20160208_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faction',
            old_name='description',
            new_name='name',
        ),
    ]
