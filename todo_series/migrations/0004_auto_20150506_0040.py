# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_series', '0003_episode_release_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='saison',
            unique_together=set([('saison_number', 'movie', 'id')]),
        ),
    ]
