# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_series', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(default=b'No title', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='saison',
            name='saison_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='saison',
            unique_together=set([('saison_number', 'movie')]),
        ),
    ]
