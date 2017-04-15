#! /usr/bin/env python
# Author: Ziyang Jia
# E-mail: ziyang.jia@gmail.com

from django.db import models
# from models import *
import csv

# main entrance for reading
def readData(data_name):
    return {
        'directed edge': readDirectedEdge(),
        'twitter user': readTwitterUsers(),
    }[data_name]

# print readTwitterUsers()
def readTwitterUsers():
    data = []
    with open('F:/Workspace/Rutgers/intro_to_alg/final_proj/src/TwitterBiconnectedGraph/website/data/twitterUser.csv') as csvfile:
        t_reader = list(csv.reader(csvfile))
        if t_reader[0][0][0] < '0' or t_reader[0][0][0] > '9':
            t_reader = t_reader[1:]
        for t_row in t_reader:
            data.append(t_row)
    return data

# print(readData('directed edge'))
def readDirectedEdge():
    data = []
    with open('F:/Workspace/Rutgers/intro_to_alg/final_proj/src/TwitterBiconnectedGraph/website/data/directedEdge.csv') as csvfile:
        t_reader = list(csv.reader(csvfile))
        if t_reader[0][0][0] < '0' or t_reader[0][0][0] > '9':
            t_reader = t_reader[1:]
        for t_row in t_reader:
            for i in range(len(t_row)):
                t_row[i] = int(t_row[i])    # transform to int
            data.append(t_row)
    return data