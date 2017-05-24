# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import bio.models.core


class Migration(migrations.Migration):

    dependencies = [
        ('askbot', '0013_auto_20161024_0010'),
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('askbot.tag',),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=bio.models.core.image_upload_to),
        ),
    ]
