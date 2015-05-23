# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_app', '0004_auto_20150517_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='user_id',
        ),
        migrations.AddField(
            model_name='material',
            name='user_id',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='question',
            name='track_id',
        ),
        migrations.AddField(
            model_name='question',
            name='track_id',
            field=models.ManyToManyField(to='new_app.Track'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
