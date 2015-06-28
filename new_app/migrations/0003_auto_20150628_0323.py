# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_auto_20150620_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(default=b'Approved', max_length=10, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected')]),
        ),
        migrations.AlterField(
            model_name='material',
            name='status',
            field=models.CharField(default=b'Approved', max_length=10, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(default=b'Approved', max_length=10, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected')]),
        ),
    ]
