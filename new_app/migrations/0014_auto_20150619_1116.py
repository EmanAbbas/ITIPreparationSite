# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import new_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0013_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.ImageField(null=True, upload_to=new_app.models.get_upload_file_name, blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.CharField(default=b'Pending', max_length=10, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(null=True, upload_to=new_app.models.get_upload_file_name, blank=True),
        ),
    ]
