# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='status',
            field=models.CharField(default=b'Pending', max_length=10, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected')]),
        ),
        migrations.AlterField(
            model_name='material',
            name='type',
            field=models.CharField(default=b'TRACK', max_length=10, choices=[(b'IQ', b'IQ'), (b'EN', b'English'), (b'SOFT', b'Soft Skills'), (b'TRACK', b'Track')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(default=b'TRACK', max_length=10, choices=[(b'IQ', b'IQ'), (b'EN', b'English'), (b'FAQ', b'FAQ'), (b'SOFT', b'Soft Skills'), (b'TRACK', b'Track')]),
        ),
    ]
