# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import bio.models.core


class Migration(migrations.Migration):

    dependencies = [
        ('contribute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantimage',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to=bio.models.core.image_upload_to),
        ),
    ]
