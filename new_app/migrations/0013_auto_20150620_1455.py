# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_app', '0012_auto_20150619_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='voteDownUsers',
            field=models.ManyToManyField(related_name='materialDownVotes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='material',
            name='voteUpUsers',
            field=models.ManyToManyField(related_name='materialUpVotes', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
