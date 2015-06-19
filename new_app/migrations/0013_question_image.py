# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import new_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0012_auto_20150618_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(null=True, upload_to=new_app.models.get_upload_file_name),
        ),
    ]
