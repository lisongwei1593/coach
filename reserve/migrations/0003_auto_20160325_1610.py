# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0002_auto_20160325_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservetime',
            old_name='time',
            new_name='reserve_time',
        ),
    ]
