# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0006_auto_20150509_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='short_name',
            field=models.CharField(max_length=10),
        ),
    ]
