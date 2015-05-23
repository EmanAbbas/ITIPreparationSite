# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0006_auto_20150523_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='track_id',
            field=models.ManyToManyField(to='new_app.Track', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='track_id',
            field=models.ManyToManyField(to='new_app.Track', blank=True),
        ),
    ]
