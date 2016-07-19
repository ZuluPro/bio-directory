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
                ('name', models.CharField(help_text='Common name, example: tomato.', max_length=50, verbose_name='name')),
                ('latin_name', models.CharField(max_length=100, null=True, verbose_name='latin name', blank=True)),
                ('variety', models.CharField(max_length=50, null=True, verbose_name='variety', blank=True)),
                ('description', models.TextField(help_text='How is the plant.', verbose_name='description', blank=True)),
                ('lifecycle', models.CharField(blank=True, max_length=20, null=True, verbose_name='lifecycle', choices=[('perennial', 'Perennial'), ('annual', 'Annual'), ('biennials', 'Biennials')])),
                ('seedling_description', models.TextField(help_text='How to seed.', null=True, verbose_name='seedling description', blank=True)),
                ('seedling_start', models.PositiveSmallIntegerField(blank=True, help_text='When start to seed.', null=True, verbose_name='seedling start month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('seedling_end', models.PositiveSmallIntegerField(blank=True, help_text='When end to seed.', null=True, verbose_name='seedling end month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('germination_period', models.PositiveSmallIntegerField(help_text='In days.', null=True, verbose_name='germination time', blank=True)),
                ('planting_description', models.TextField(help_text='How to plant.', null=True, verbose_name='planting description', blank=True)),
                ('planting_start', models.PositiveSmallIntegerField(blank=True, help_text='When start to plant.', null=True, verbose_name='planting start month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('planting_end', models.PositiveSmallIntegerField(blank=True, help_text='When end to plant.', null=True, verbose_name='planting end month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('growth_period', models.PositiveSmallIntegerField(help_text='In days.', null=True, verbose_name='growth time', blank=True)),
                ('growth_description', models.TextField(help_text='How plant growths.', null=True, verbose_name='growth description', blank=True)),
                ('growth_maintenance', models.TextField(help_text='How to take care.', null=True, verbose_name='growth maintenance', blank=True)),
                ('blossom_period', models.PositiveSmallIntegerField(help_text='In days.', null=True, verbose_name='blossom time', blank=True)),
                ('blossom_description', models.TextField(help_text='How plant flower.', null=True, verbose_name='blossom description', blank=True)),
                ('blossom_maintenance', models.TextField(help_text='How take care of blossom.', null=True, verbose_name='blossom maintenance', blank=True)),
                ('harvest_description', models.TextField(help_text='How to harvest.', null=True, verbose_name='harvest description', blank=True)),
                ('harvest_start', models.PositiveSmallIntegerField(blank=True, help_text='When start harvest.', null=True, verbose_name='harvest start month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('harvest_end', models.PositiveSmallIntegerField(blank=True, help_text='When end harvest.', null=True, verbose_name='harvest end month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('environment_description', models.TextField(help_text='What is the best environment.', null=True, verbose_name='environment description', blank=True)),
                ('temp_min', models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='minimum temperature', blank=True)),
                ('temp_optimal_day', models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='optimal day temperature', blank=True)),
                ('temp_optimal_night', models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='optimal ngiht temperature', blank=True)),
                ('temp_max', models.SmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='maximum temperature', blank=True)),
                ('humidity_min', models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='minimum humidity', blank=True)),
                ('humidity_max', models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='maximum humidity', blank=True)),
                ('density', models.PositiveSmallIntegerField(help_text='In unit by m2.', null=True, verbose_name='optimal density', blank=True)),
                ('exposition', models.CharField(blank=True, max_length=15, null=True, verbose_name='exposition', choices=[('full_sunlight', 'full sunlight'), ('partial shade', 'partial shade'), ('shade', 'shade')])),
                ('exposition_time', models.PositiveSmallIntegerField(help_text='In hours', null=True, verbose_name='exposition time', blank=True)),
                ('ph_min', models.PositiveSmallIntegerField(null=True, verbose_name='minimum PH', blank=True)),
                ('ph_max', models.PositiveSmallIntegerField(null=True, verbose_name='maximum PH', blank=True)),
                ('nitrogen', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('phosphorus', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('potassium', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('food', models.BooleanField(default=True, verbose_name='is food')),
                ('toxic', models.BooleanField(verbose_name='is toxic')),
                ('green_manure', models.BooleanField(default=False, verbose_name='is green manure')),
                ('after', models.ManyToManyField(help_text='What to plant after this plant', related_name='_plant_after_+', verbose_name='plant after', to='bio.Plant', blank=True)),
                ('before', models.ManyToManyField(help_text='What to plant before this plant.', related_name='_plant_before_+', verbose_name='plant before', to='bio.Plant', blank=True)),
                ('dislike', models.ManyToManyField(help_text='Plants with bad association', related_name='_plant_dislike_+', verbose_name='bad with', to='bio.Plant', blank=True)),
                ('illustration', models.ForeignKey(related_name='plant_illustrations', blank=True, to='bio.Image', help_text='Image showed for illustrate the plant.', null=True, verbose_name='illustration')),
                ('images', models.ManyToManyField(help_text='Gallery of images representing the plant.', to='bio.Image', verbose_name='images', blank=True)),
                ('like', models.ManyToManyField(help_text='Plants with beneficial association', related_name='_plant_like_+', verbose_name='good with', to='bio.Plant', blank=True)),
                ('pathologies', models.ManyToManyField(help_text='Disease affecting the plant.', to='bio.Pathology', verbose_name='pathologies', blank=True)),
                ('pests', models.ManyToManyField(help_text='Organisms that cause nuisance and epidemic disease.', to='bio.Pest', verbose_name='pests', blank=True)),
            ],
            options={
                'verbose_name': 'plant',
                'verbose_name_plural': 'plants',
            },
        ),
        migrations.AlterUniqueTogether(
            name='plant',
            unique_together=set([('name', 'variety')]),
        ),
    ]
