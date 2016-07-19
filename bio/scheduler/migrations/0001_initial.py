# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_event_color_event'),
        ('bio_items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='schedule.Event')),
                ('areas', models.ManyToManyField(to='bio_items.Area', verbose_name='areas', blank=True)),
                ('plants', models.ManyToManyField(to='bio_items.PlantItem', verbose_name='plants', blank=True)),
            ],
            options={
                'verbose_name': 'action',
                'verbose_name_plural': 'action',
            },
            bases=('schedule.event',),
        ),
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
            ],
            options={
                'verbose_name': 'action type',
                'verbose_name_plural': 'action types',
            },
        ),
        migrations.AddField(
            model_name='action',
            name='type',
            field=models.ForeignKey(verbose_name='type', to='bio_scheduler.ActionType'),
        ),
    ]
