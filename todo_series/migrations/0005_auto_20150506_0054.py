# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_series', '0004_auto_20150506_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='identifiant',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='saison',
            unique_together=set([]),
        ),
    ]
