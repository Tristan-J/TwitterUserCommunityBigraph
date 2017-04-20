# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 03:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0006_auto_20170419_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectedEdge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='count of at times')),
            ],
            options={
                'db_table': 'community_edge',
            },
        ),
        migrations.CreateModel(
            name='TwitterMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='content of a Twitter message')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name of Twitter user')),
                ('sticker', models.CharField(max_length=50, verbose_name='sticker, like "superman of sporting"')),
            ],
            options={
                'db_table': 'twitter_user',
            },
        ),
        migrations.AddField(
            model_name='twittermessage',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_message', to='website.TwitterUser'),
        ),
        migrations.AddField(
            model_name='directededge',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_edge', to='website.TwitterUser'),
        ),
        migrations.AddField(
            model_name='directededge',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_edge', to='website.TwitterUser'),
        ),
    ]
