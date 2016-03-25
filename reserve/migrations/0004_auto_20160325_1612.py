# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_auto_20160325_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservetime',
            name='reserve_time',
            field=models.TimeField(),
        ),
    ]
