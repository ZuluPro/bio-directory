# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='blossom_description',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='blossom_maintenance',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='exposition',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='exposition_time',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='growth_description',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='harvest_description',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='planting_description',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='seedling_description',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='temp_optimal_day',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='temp_optimal_night',
        ),
    ]
