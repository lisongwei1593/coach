# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservetime',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
