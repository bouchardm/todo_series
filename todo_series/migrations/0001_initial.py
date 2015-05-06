# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('episode_name', models.CharField(max_length=200)),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imdb_id', models.CharField(max_length=200)),
                ('title', models.CharField(default=b'[No title]', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Saison',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saison_number', models.IntegerField(default=0, serialize=False)),
                ('movie', models.ForeignKey(to='todo_series.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='saison',
            field=models.ForeignKey(to='todo_series.Saison'),
        ),
    ]
