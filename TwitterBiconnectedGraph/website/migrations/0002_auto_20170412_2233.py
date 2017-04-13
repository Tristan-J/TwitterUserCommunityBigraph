# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
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
        migrations.AddField(
            model_name='twitteruser',
            name='sticker',
            field=models.CharField(default='test', max_length=50, verbose_name='sticker, like "superman of sporting"'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='directededge',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='website.TwitterUser'),
        ),
        migrations.AddField(
            model_name='directededge',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='website.TwitterUser'),
        ),
    ]