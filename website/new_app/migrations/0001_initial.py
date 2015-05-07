# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=1200)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=100)),
                ('answer', models.TextField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_type', models.CharField(max_length=1, choices=[(b'HR', b'HR'), (b'Technical', b'Technical'), (b'Final', b'Final_interview')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='track_id',
            field=models.ForeignKey(to='new_app.Track'),
        ),
        migrations.AddField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(to='new_app.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='type_name',
            field=models.ForeignKey(to='new_app.Type'),
        ),
        migrations.AddField(
            model_name='material',
            name='track_id',
            field=models.ManyToManyField(to='new_app.Track'),
        ),
        migrations.AddField(
            model_name='material',
            name='user_id',
            field=models.ManyToManyField(to='new_app.User'),
        ),
    ]
