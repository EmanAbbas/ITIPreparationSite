# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0005_material_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='short_name',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='track',
            name='description',
            field=models.TextField(),
        ),
    ]
