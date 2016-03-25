# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0004_auto_20160325_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservetime',
            options={'verbose_name': '\u9884\u7ea6\u65f6\u95f4\u70b9', 'verbose_name_plural': '\u9884\u7ea6\u65f6\u95f4\u70b9'},
        ),
        migrations.AddField(
            model_name='reserve',
            name='reserve_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 25, 8, 38, 1, 605000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
