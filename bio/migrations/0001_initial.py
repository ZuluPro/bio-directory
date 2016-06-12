# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='Pathology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('latin_name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(max_length=2000, null=True, blank=True)),
                ('symptom', models.TextField(max_length=300, null=True, blank=True)),
                ('treatment', models.TextField(max_length=5000, blank=True)),
                ('illustration', models.ForeignKey(related_name='pathology_illustrations', blank=True, to='bio.Image', null=True)),
                ('images', models.ManyToManyField(to='bio.Image', blank=True)),
            ],
            options={
                'verbose_name': 'pathology',
                'verbose_name_plural': 'pathologies',
            },
        ),
        migrations.CreateModel(
            name='Pest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('latin_name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(max_length=2000, null=True, blank=True)),
                ('symptom', models.TextField(max_length=300, null=True, blank=True)),
                ('treatment', models.TextField(max_length=5000, blank=True)),
                ('illustration', models.ForeignKey(related_name='pest_illustrations', blank=True, to='bio.Image', null=True)),
                ('images', models.ManyToManyField(to='bio.Image', blank=True)),
            ],
            options={
                'verbose_name': 'pest',
                'verbose_name_plural': 'pests',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('latin_name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('planting_description', models.TextField(null=True, blank=True)),
                ('planting_start', models.SmallIntegerField(blank=True, null=True, choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('planting_end', models.SmallIntegerField(blank=True, null=True, choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('growth_description', models.TextField(null=True, blank=True)),
                ('growth_period', models.SmallIntegerField(null=True, blank=True)),
                ('blossom_description', models.TextField(null=True, blank=True)),
                ('blossom_period', models.SmallIntegerField(null=True, blank=True)),
                ('harvest_description', models.TextField(null=True, blank=True)),
                ('harvest_start', models.SmallIntegerField(blank=True, null=True, choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('harvest_end', models.SmallIntegerField(blank=True, null=True, choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('environment_description', models.TextField(null=True, blank=True)),
                ('temp_min', models.SmallIntegerField(null=True, blank=True)),
                ('temp_max', models.SmallIntegerField(null=True, blank=True)),
                ('humidity_min', models.SmallIntegerField(null=True, blank=True)),
                ('humidity_max', models.SmallIntegerField(null=True, blank=True)),
                ('heliophilous', models.NullBooleanField()),
                ('food', models.BooleanField()),
                ('toxic', models.BooleanField()),
                ('dislike', models.ManyToManyField(related_name='_plant_dislike_+', to='bio.Plant', blank=True)),
                ('illustration', models.ForeignKey(related_name='plant_illustrations', blank=True, to='bio.Image', null=True)),
                ('images', models.ManyToManyField(to='bio.Image', blank=True)),
                ('like', models.ManyToManyField(related_name='_plant_like_+', to='bio.Plant', blank=True)),
                ('pathologies', models.ManyToManyField(to='bio.Pathology', blank=True)),
                ('pests', models.ManyToManyField(to='bio.Pest', blank=True)),
            ],
            options={
                'verbose_name': 'plant',
                'verbose_name_plural': 'plants',
            },
        ),
    ]
