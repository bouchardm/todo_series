# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_series', '0005_auto_20150506_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='identifiant',
        ),
    ]
