# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_app', '0008_auto_20150530_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='voteDownUsers',
            field=models.ManyToManyField(related_name='questionDownVotes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='voteUpUsers',
            field=models.ManyToManyField(related_name='questionUpVotes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
