# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio_guide', '0001_initial'),
        ('bio_items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantitem',
            name='planting_area',
        ),
        migrations.RemoveField(
            model_name='plantitem',
            name='planting_date',
        ),
        migrations.AddField(
            model_name='plantitem',
            name='blossom_guide',
            field=models.ForeignKey(related_name='plant_blossom', blank=True, to='bio_guide.Guide', help_text='How take care of blossom', null=True, verbose_name='blossom guide'),
        ),
        migrations.AddField(
            model_name='plantitem',
            name='germination_guide',
            field=models.ForeignKey(related_name='germinated_plant', blank=True, to='bio_guide.Guide', help_text='How to germinate', null=True, verbose_name='germination guide'),
        ),
        migrations.AddField(
            model_name='plantitem',
            name='real_leaf_date',
            field=models.DateField(help_text='When the has its first real leaves', null=True, verbose_name='first real leaves date', blank=True),
        ),
        migrations.AddField(
            model_name='plantitem',
            name='transplanting_area',
            field=models.ForeignKey(related_name='planted', blank=True, to='bio_items.Area', help_text='Where it has been transplanted', null=True, verbose_name='transplanting area'),
        ),
        migrations.AddField(
            model_name='plantitem',
            name='transplanting_date',
            field=models.DateField(help_text='When it has been transplanted for real growth', null=True, verbose_name='transplanting date', blank=True),
        ),
        migrations.AddField(
            model_name='plantitem',
            name='transplanting_guide',
            field=models.ForeignKey(related_name='transplanted_plant', blank=True, to='bio_guide.Guide', help_text='How do you plant', null=True, verbose_name='transplanting guide'),
        ),
        migrations.AlterField(
            model_name='area',
            name='type',
            field=models.CharField(max_length=30, verbose_name='type', choices=[('outside', 'outside'), ('inside', 'inside'), ('greenhouse', 'greenhouse')]),
        ),
        migrations.AlterField(
            model_name='plantitem',
            name='seedling_area',
            field=models.ForeignKey(related_name='seedling', blank=True, to='bio_items.Area', help_text='Where it has been sown', null=True, verbose_name='seedling area'),
        ),
        migrations.AlterField(
            model_name='plantitem',
            name='stage',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='stage', choices=[('sow', 'sow'), ('germination', 'germination'), ('juvenile', 'juvenile'), ('adult', 'adult'), ('blossom', 'blossom'), ('fruit', 'fruit'), ('dormant', 'dormant')]),
        ),
    ]
