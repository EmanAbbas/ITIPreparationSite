# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_auto_20150516_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='track_id',
            field=models.ForeignKey(blank=True, to='new_app.Track', null=True),
        ),
    ]
