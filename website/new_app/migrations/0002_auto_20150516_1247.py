# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='track_id',
            field=models.ForeignKey(to='new_app.Track', blank=True),
            preserve_default=True,
        ),
    ]
