# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPlant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.TextField(max_length=1000, verbose_name=b'reference', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('validated', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('declined_by', models.ManyToManyField(related_name='_newplant_declined_by_+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ManyToManyField(related_name='_newplant_validated_by_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'new plant',
                'verbose_name_plural': 'new plants',
            },
        ),
        migrations.CreateModel(
            name='PlantImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.TextField(max_length=1000, verbose_name=b'reference', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('validated', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'')),
                ('description', models.TextField(null=True, blank=True)),
                ('declined_by', models.ManyToManyField(related_name='_plantimage_declined_by_+', to=settings.AUTH_USER_MODEL)),
                ('plant', models.ForeignKey(to='bio.Plant')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ManyToManyField(related_name='_plantimage_validated_by_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'plant image',
                'verbose_name_plural': 'plant images',
            },
        ),
        migrations.CreateModel(
            name='PlantQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.TextField(max_length=1000, verbose_name=b'reference', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('validated', models.BooleanField(default=False)),
                ('fieldname', models.CharField(max_length=50)),
                ('response', models.CharField(max_length=255)),
                ('declined_by', models.ManyToManyField(related_name='_plantquestion_declined_by_+', to=settings.AUTH_USER_MODEL)),
                ('plant', models.ForeignKey(to='bio.Plant')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ManyToManyField(related_name='_plantquestion_validated_by_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'plant question',
                'verbose_name_plural': 'plant questions',
            },
        ),
    ]
