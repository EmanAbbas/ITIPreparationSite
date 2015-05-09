# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_app', '0003_auto_20150509_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='material',
            name='track_id',
            field=models.ManyToManyField(to='new_app.Track'),
        ),
        migrations.AddField(
            model_name='material',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
