# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import new_app.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField(verbose_name=b'Answer')),
                ('status', models.CharField(default=b'Pending', max_length=10, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected')])),
                ('image', models.ImageField(null=True, upload_to=new_app.models.get_upload_file_name, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('type', models.CharField(default=b'TRACK', max_length=10, choices=[(b'IQ', b'IQ'), (b'EN', b'English'), (b'TRACK', b'Track')])),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=1200)),
                ('date', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=100)),
                ('type', models.CharField(default=b'TRACK', max_length=10, choices=[(b'IQ', b'IQ'), (b'EN', b'English'), (b'FAQ', b'FAQ'), (b'TRACK', b'Track')])),
                ('status', models.CharField(default=b'Pending', max_length=10, choices=[(b'Pending', b'Pending'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected')])),
                ('image', models.ImageField(null=True, upload_to=new_app.models.get_upload_file_name, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_type', models.CharField(max_length=1, choices=[(b'HR', b'HR'), (b'Technical', b'Technical'), (b'Final', b'Final_interview')])),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='track_id',
            field=models.ManyToManyField(to='new_app.Track', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
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
        migrations.AddField(
            model_name='post',
            name='type_name',
            field=models.ForeignKey(to='new_app.Type'),
        ),
        migrations.AddField(
            model_name='material',
            name='track_id',
            field=models.ManyToManyField(to='new_app.Track', blank=True),
        ),
        migrations.AddField(
            model_name='material',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
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
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(related_name='answers', to='new_app.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
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
