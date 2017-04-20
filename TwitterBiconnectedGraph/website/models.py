#! /usr/bin/env python
# Author: Ziyang Jia
# E-mail: ziyang.jia@gmail.com

from django.db import models

# Table of twitter users
class TwitterUser(models.Model):
    name = models.CharField('name of Twitter user', max_length=50)
    sticker = models.CharField('sticker, like "superman of sporting"', max_length=50)

    class Meta:
        db_table = 'twitter_user'

    def __str__(self):
        return self.name

# Table of twitter messages
class TwitterMessage(models.Model):
    message = models.TextField('content of a Twitter message')
    source = models.ForeignKey(TwitterUser, related_name='source_message', on_delete=models.CASCADE)

    class Meta:
        db_table = 'twitter_message'

    def __str__(self):
        return self.name

# Table of directed edges
# to avoid the redundance, we'll not create an undirected-edge-table
class DirectedEdge(models.Model):
    source  = models.ForeignKey(TwitterUser, related_name='source_edge', on_delete=models.CASCADE)
    target  = models.ForeignKey(TwitterUser, related_name='target_edge', on_delete=models.CASCADE)
    count   = models.IntegerField('count of at times')

    class Meta:
        db_table = 'community_edge'

    def __str__(self):
        return self.source + ',\t' + self.target
