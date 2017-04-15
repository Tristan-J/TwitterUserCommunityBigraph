#! /usr/bin/env python
# Author: Ziyang Jia
# E-mail: ziyang.jia@gmail.com

from django.http import HttpResponse

def index(response):
    return HttpResponse('<h1>This is my first html page for TwitterUser BCG!</h1>')