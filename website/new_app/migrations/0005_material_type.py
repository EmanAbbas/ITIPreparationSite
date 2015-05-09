# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0004_auto_20150509_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='type',
            field=models.CharField(default=b'TRACK', max_length=10, choices=[(b'IQ', b'IQ'), (b'EN', b'English'), (b'TRACK', b'Track')]),
        ),
    ]
