# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0003_auto_20160703_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=30, verbose_name='type', choices=[('outside', 'outside'), ('inside', 'inside'), ('greenhouse', 'inside')])),
                ('soil_type', models.CharField(blank=True, max_length=30, null=True, verbose_name='soil type', choices=[('potting', 'potting soil'), ('clay', 'clay'), ('sand', 'sand'), ('silt', 'silt')])),
                ('ph', models.PositiveSmallIntegerField(null=True, verbose_name='PH', blank=True)),
                ('surface', models.PositiveSmallIntegerField(help_text='In m2.', null=True, verbose_name='surface', blank=True)),
                ('morning_temp', models.PositiveSmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='morning temperature', blank=True)),
                ('day_temp', models.PositiveSmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='day temperature', blank=True)),
                ('night_temp', models.PositiveSmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='night temperature', blank=True)),
                ('morning_humidity', models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='day humidity', blank=True)),
                ('day_humidity', models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='day humidity', blank=True)),
                ('night_humidity', models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='night humidity', blank=True)),
                ('morning_exposition', models.CharField(blank=True, max_length=15, null=True, verbose_name='morning exposition', choices=[('full_sunlight', 'full sunlight'), ('partial shade', 'partial shade'), ('shade', 'shade')])),
                ('afternoon_exposition', models.CharField(blank=True, max_length=15, null=True, verbose_name='afternoon exposition', choices=[('full_sunlight', 'full sunlight'), ('partial shade', 'partial shade'), ('shade', 'shade')])),
                ('exposition_time', models.PositiveSmallIntegerField(help_text='In hours', null=True, verbose_name='exposition time', blank=True)),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'areas',
            },
        ),
        migrations.CreateModel(
            name='PlantItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stage', models.CharField(blank=True, max_length=15, null=True, verbose_name='stage', choices=[('sow', 'sow'), ('germination', 'germination'), ('seedling', 'adult'), ('flowering', 'fruit'), ('dormant', 'dormant')])),
                ('seedling_date', models.DateField(help_text='When the seed has been planted', null=True, verbose_name='seedling date', blank=True)),
                ('planting_date', models.DateField(help_text='When it has been planted to growth', null=True, verbose_name='planting date', blank=True)),
                ('blossom_start_date', models.DateField(help_text='When it has its first flower', null=True, verbose_name='blossom date', blank=True)),
                ('harvest_start_date', models.DateField(help_text='When it has its usable element', null=True, verbose_name='harvest date', blank=True)),
                ('death_date', models.DateField(help_text='When it is considered as dead', null=True, verbose_name='death date', blank=True)),
                ('planting_area', models.ForeignKey(related_name='planted', blank=True, to='bio_items.Area', help_text='Where it has been planted', null=True, verbose_name='planting area')),
                ('seedling_area', models.ForeignKey(related_name='sown', blank=True, to='bio_items.Area', help_text='Where it has been sown', null=True, verbose_name='seedling area')),
                ('type', models.ForeignKey(to='bio.Plant')),
            ],
            options={
                'verbose_name': 'plant',
                'verbose_name_plural': 'plants',
            },
        ),
    ]
