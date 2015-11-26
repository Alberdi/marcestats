# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('minutes', models.IntegerField(null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('game', models.ForeignKey(to='stats.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(null=True, blank=True)),
                ('winner', models.NullBooleanField()),
                ('faction', models.ForeignKey(to='stats.Faction', null=True)),
                ('play', models.ForeignKey(to='stats.Play')),
                ('players', models.ManyToManyField(to='stats.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('game', models.ForeignKey(to='stats.Game')),
            ],
        ),
        migrations.AddField(
            model_name='play',
            name='variant',
            field=models.ForeignKey(to='stats.Variant', null=True),
        ),
        migrations.AddField(
            model_name='faction',
            name='game',
            field=models.ForeignKey(to='stats.Game'),
        ),
    ]
