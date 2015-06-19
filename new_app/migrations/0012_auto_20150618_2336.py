# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0011_auto_20150618_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 23, 35, 20, 258091, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 23, 35, 35, 130443, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 23, 35, 43, 349991, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 23, 35, 50, 48782, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 23, 35, 56, 690693, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 23, 36, 3, 858114, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 23, 36, 10, 55397, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 23, 36, 15, 797809, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(default=b'Pending', max_length=10, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected')]),
        ),
    ]
