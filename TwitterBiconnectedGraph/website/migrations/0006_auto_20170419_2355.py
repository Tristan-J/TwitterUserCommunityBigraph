# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170419_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directededge',
            name='source',
        ),
        migrations.RemoveField(
            model_name='directededge',
            name='target',
        ),
        migrations.RemoveField(
            model_name='twittermessage',
            name='source',
        ),
        migrations.DeleteModel(
            name='DirectedEdge',
        ),
        migrations.DeleteModel(
            name='TwitterMessage',
        ),
        migrations.DeleteModel(
            name='TwitterUser',
        ),
    ]
