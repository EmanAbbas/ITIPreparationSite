# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_app', '0009_auto_20150530_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='voteDownUsers',
            field=models.ManyToManyField(related_name='answerDownVotes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='voteUpUsers',
            field=models.ManyToManyField(related_name='answerUpVotes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
