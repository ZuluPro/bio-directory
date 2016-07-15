# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_auto_20160703_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='density',
            field=models.PositiveSmallIntegerField(help_text='In unit by m2.', null=True, verbose_name='optimal density', blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='green_manure',
            field=models.BooleanField(default=False, verbose_name='is green manure'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='food',
            field=models.BooleanField(default=True, verbose_name='is food'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temp_max',
            field=models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='maximum temperature', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temp_min',
            field=models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='minimum temperature', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temp_optimal_day',
            field=models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='optimal day temperature', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temp_optimal_night',
            field=models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='optimal ngiht temperature', blank=True),
        ),
    ]
