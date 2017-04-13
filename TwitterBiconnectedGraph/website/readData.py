#! /usr/bin/env python
# Author: Ziyang Jia
# E-mail: ziyang.jia@gmail.com

from django.db import models
import csv

# main entrance for reading
def readData(data_name):
    return {
        'directed edge': readDirectedEdge(),
    }[data_name]

def readDirectedEdge():
    data = []
    with open('./data/directedEdge.csv', newline='') as csvfile:
        # t_reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
        t_reader = csv.reader(csvfile)
        for t_row in t_reader:
            data.append(t_row)
        return data


# print(readData('directed edge'))