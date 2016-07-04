# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_auto_20160702_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='after',
            field=models.ManyToManyField(help_text='What to plant after this plant', related_name='_plant_after_+', verbose_name='plant after', to='bio.Plant', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='before',
            field=models.ManyToManyField(help_text='What to plant before this plant.', related_name='_plant_before_+', verbose_name='plant before', to='bio.Plant', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='blossom_description',
            field=models.TextField(help_text='How plant flower.', null=True, verbose_name='blossom description', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='blossom_maintenance',
            field=models.TextField(help_text='How take care of blossom.', null=True, verbose_name='blossom maintenance', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='blossom_period',
            field=models.PositiveSmallIntegerField(help_text='In days.', null=True, verbose_name='blossom time', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='description',
            field=models.TextField(help_text='How is the plant.', verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='dislike',
            field=models.ManyToManyField(help_text='Plants with bad association', related_name='_plant_dislike_+', verbose_name='bad with', to='bio.Plant', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='environment_description',
            field=models.TextField(help_text='What is the best environment.', null=True, verbose_name='environment description', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='exposition',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='exposition', choices=[('full_sunlight', 'full sunlight'), ('partial shade', 'partial shade'), ('shade', 'shade')]),
        ),
        migrations.AlterField(
            model_name='plant',
            name='exposition_time',
            field=models.PositiveSmallIntegerField(help_text='In hours', null=True, verbose_name='exposition time', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='food',
            field=models.BooleanField(verbose_name='is food'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='germination_period',
            field=models.PositiveSmallIntegerField(help_text='In days.', null=True, verbose_name='germination time', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='growth_description',
            field=models.TextField(help_text='How plant growths.', null=True, verbose_name='growth description', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='growth_maintenance',
            field=models.TextField(help_text='How to take care.', null=True, verbose_name='growth maintenance', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='growth_period',
            field=models.PositiveSmallIntegerField(help_text='In days.', null=True, verbose_name='growth time', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='harvest_description',
            field=models.TextField(help_text='How to harvest.', null=True, verbose_name='harvest description', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='harvest_end',
            field=models.PositiveSmallIntegerField(blank=True, help_text='When end harvest.', null=True, verbose_name='harvest end month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AlterField(
            model_name='plant',
            name='harvest_start',
            field=models.PositiveSmallIntegerField(blank=True, help_text='When start harvest.', null=True, verbose_name='harvest start month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AlterField(
            model_name='plant',
            name='humidity_max',
            field=models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='maximum humidity', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='humidity_min',
            field=models.PositiveSmallIntegerField(help_text='In %.', null=True, verbose_name='minimum humidity', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='illustration',
            field=models.ForeignKey(related_name='plant_illustrations', blank=True, to='bio.Image', help_text='Image showed for illustrate the plant.', null=True, verbose_name='illustration'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='images',
            field=models.ManyToManyField(help_text='Gallery of images representing the plant.', to='bio.Image', verbose_name='images', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='latin_name',
            field=models.CharField(max_length=100, null=True, verbose_name='latin name', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='lifecycle',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='lifecycle', choices=[('perennial', 'Perennial'), ('annual', 'Annual'), ('biennials', 'Biennials')]),
        ),
        migrations.AlterField(
            model_name='plant',
            name='like',
            field=models.ManyToManyField(help_text='Plants with beneficial association', related_name='_plant_like_+', verbose_name='good with', to='bio.Plant', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(help_text='Common name, example: tomato.', max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='nitrogen',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='pathologies',
            field=models.ManyToManyField(help_text='Disease affecting the plant.', to='bio.Pathology', verbose_name='pathologies', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='pests',
            field=models.ManyToManyField(help_text='Organisms that cause nuisance and epidemic disease.', to='bio.Pest', verbose_name='pests', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='ph_max',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='maximum PH', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='ph_min',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='minimum PH', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='phosphorus',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='planting_description',
            field=models.TextField(help_text='How to plant.', null=True, verbose_name='planting description', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='planting_end',
            field=models.PositiveSmallIntegerField(blank=True, help_text='When end to plant.', null=True, verbose_name='planting end month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AlterField(
            model_name='plant',
            name='planting_start',
            field=models.PositiveSmallIntegerField(blank=True, help_text='When start to plant.', null=True, verbose_name='planting start month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AlterField(
            model_name='plant',
            name='potassium',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='seedling_description',
            field=models.TextField(help_text='How to seed.', null=True, verbose_name='seedling description', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='seedling_end',
            field=models.PositiveSmallIntegerField(blank=True, help_text='When end to seed.', null=True, verbose_name='seedling end month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AlterField(
            model_name='plant',
            name='seedling_start',
            field=models.PositiveSmallIntegerField(blank=True, help_text='When start to seed.', null=True, verbose_name='seedling start month', choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temp_max',
            field=models.PositiveSmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='maximum temperature', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temp_min',
            field=models.PositiveSmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='minimum temperature', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temp_optimal_day',
            field=models.PositiveSmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='optimal day temperature', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temp_optimal_night',
            field=models.PositiveSmallIntegerField(help_text='In \xb0C.', null=True, verbose_name='optimal ngiht temperature', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='toxic',
            field=models.BooleanField(verbose_name='is toxic'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='variety',
            field=models.CharField(max_length=50, null=True, verbose_name='variety', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='plant',
            unique_together=set([('name', 'variety')]),
        ),
    ]
