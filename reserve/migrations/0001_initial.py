# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
            ],
            options={
                'verbose_name': '\u6559\u7ec3',
                'verbose_name_plural': '\u6559\u7ec3',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('coach', models.ForeignKey(related_name='reserve_coach', verbose_name='\u6559\u7ec3', to='reserve.Coach')),
            ],
            options={
                'verbose_name': '\u9884\u7ea6',
                'verbose_name_plural': '\u9884\u7ea6',
            },
        ),
        migrations.CreateModel(
            name='ReserveInterval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interval', models.IntegerField()),
            ],
            options={
                'verbose_name': '\u9884\u7ea6\u95f4\u9694',
                'verbose_name_plural': '\u9884\u7ea6\u95f4\u9694',
            },
        ),
        migrations.CreateModel(
            name='ReserveTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
            ],
            options={
                'verbose_name': '\u5b66\u5458',
                'verbose_name_plural': '\u5b66\u5458',
            },
        ),
        migrations.AddField(
            model_name='reserve',
            name='student',
            field=models.ForeignKey(related_name='reserve_coach', verbose_name='\u5b66\u5458', to='reserve.Student'),
        ),
    ]
