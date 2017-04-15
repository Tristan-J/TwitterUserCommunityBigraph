#! /usr/bin/env python
# Author: Ziyang Jia
# E-mail: ziyang.jia@gmail.com

from django.db import models
from .readData import readData

# Table of twitter users
class TwitterUser(models.Model):
    name = models.CharField('name of Twitter user', max_length=50)
    sticker = models.CharField('sticker, like "superman of sporting"', max_length=50)

    class Meta:
        db_table = 'twitter_user'

    def __str__(self):
        return self.name


# Table of directed edges
# to avoid the redundance, we'll not create an undirected-edge-table
class DirectedEdge(models.Model):
    source  = models.ForeignKey(TwitterUser, related_name='source', on_delete=models.CASCADE)
    target  = models.ForeignKey(TwitterUser, related_name='target', on_delete=models.CASCADE)
    count   = models.IntegerField('count of at times')

    class Meta:
        db_table = 'community_edge'

    def __str__(self):
        return self.source + ',\t' + self.target

# Insert data to database
def insertData():
    # insert TwitterUser
    data = readData('twitter user')
    user_list = []
    for i in range(len(data)):
        t_user = TwitterUser.objects.create(
            name    = data[i][1],
            sticker = data[i][2]
        )
        t_user.save()
        user_list.append(t_user)

    # insert DirectedEdge
    data = readData('directed edge')
    for i in range(len(data)):
        t_edge = DirectedEdge.objects.create(
            source = user_list[data[i][1]-1],
            target = user_list[data[i][2]-1],
            count  = data[i][3]
        )
        t_edge.save()

insertData()