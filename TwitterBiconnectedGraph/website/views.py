#! /usr/bin/env python
# Author: Ziyang Jia
# E-mail: ziyang.jia@gmail.com

from django.http import HttpResponse
from django.template import loader
from .readData import readData
from .models import *

def index(response):
    # insert data, only needed in the first time
    # insertData()

    all_twitter_user = TwitterUser.objects.all()

    template = loader.get_template('index/index.html')
    context = {
        'all_twitter_user': all_twitter_user,
    }

    return HttpResponse(template.render(context, response))

def twitterUser(request, user_id):
    all_twitter_user = TwitterUser.objects.filter(id=int(user_id))
    html = ''
    html += '<h1>' + str(user_id) + '</h1>'
    for twitter_user in all_twitter_user:
        html += '<h1>' + twitter_user.name + '</h1>'
    return HttpResponse(html)

def getData(request, file_name):
    content = ''
    with open('F:/Workspace/Rutgers/intro_to_alg/final_proj/src/TwitterBiconnectedGraph/website/data/twitterUser.csv', 'r') as file:
        for line in file:
            content += line
    return HttpResponse(content, content_type='text/plain')


# Insert data to database
def insertData():
    # In case repeatedly inserting same data
    TwitterUser.objects.all().delete()
    DirectedEdge.objects.all().delete()

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
