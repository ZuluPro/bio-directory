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
            name='heliophilous',
        ),
        migrations.AddField(
            model_name='plant',
            name='after',
            field=models.ManyToManyField(related_name='_plant_after_+', to='bio.Plant', blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='before',
            field=models.ManyToManyField(related_name='_plant_before_+', to='bio.Plant', blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='blossom_maintenance',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='exposition',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[(b'full_sunlight', 'full sunlight'), (b'partial shade', 'partial shade'), (b'shade', 'shade')]),
        ),
        migrations.AddField(
            model_name='plant',
            name='exposition_time',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='germination_period',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='growth_maintenance',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='lifecycle',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'perennial', 'Perennial'), (b'annual', 'Annual'), (b'biennials', 'Biennials')]),
        ),
        migrations.AddField(
            model_name='plant',
            name='nitrogen',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='ph_max',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='ph_min',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='phosphorus',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='potassium',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='seedling_description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='seedling_end',
            field=models.SmallIntegerField(blank=True, null=True, choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AddField(
            model_name='plant',
            name='seedling_start',
            field=models.SmallIntegerField(blank=True, null=True, choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AddField(
            model_name='plant',
            name='temp_optimal_day',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='temp_optimal_night',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='variety',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
