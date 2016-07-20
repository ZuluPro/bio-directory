# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_auto_20160719_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('stage', models.CharField(blank=True, max_length=15, null=True, verbose_name='stage', choices=[('germination', 'germination'), ('juvenile', 'juvenile'), ('adult', 'adult'), ('blossom', 'blossom'), ('fruit', 'fruit'), ('dormant', 'dormant')])),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('area_type', models.CharField(blank=True, max_length=30, null=True, verbose_name='type', choices=[('outside', 'outside'), ('inside', 'inside'), ('greenhouse', 'greenhouse')])),
                ('soil_type', models.CharField(blank=True, max_length=30, null=True, verbose_name='soil type', choices=[('potting', 'potting soil'), ('clay', 'clay'), ('sand', 'sand'), ('silt', 'silt')])),
                ('exposition', models.CharField(blank=True, max_length=15, null=True, verbose_name='exposition', choices=[('full_sunlight', 'full sunlight'), ('partial shade', 'partial shade'), ('shade', 'shade')])),
                ('exposition_time', models.PositiveSmallIntegerField(help_text='In hours', null=True, verbose_name='exposition time', blank=True)),
                ('humidity_min', models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='minimum humidity', blank=True)),
                ('humidity_max', models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='maximum humidity', blank=True)),
                ('temperature_min', models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='minimum temperature', blank=True)),
                ('temperature_max', models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='maximum temperature', blank=True)),
                ('illustration', models.ForeignKey(related_name='guide_illustrations', blank=True, to='bio.Image', null=True)),
                ('images', models.ManyToManyField(to='bio.Image', blank=True)),
            ],
            options={
                'verbose_name': 'guide',
                'verbose_name_plural': 'guides',
            },
        ),
    ]
