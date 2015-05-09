# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_auto_20150509_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='track_id',
        ),
        migrations.RemoveField(
            model_name='material',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='material',
            name='link',
            field=models.URLField(),
        ),
    ]
