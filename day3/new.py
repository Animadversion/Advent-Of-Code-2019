#!/usr/bin/env python3

import time,json,re

location = {'x':0, 'y':0}
paths = {}
positions = []
i = 1
currentpath = 1

with open("input", 'r') as f:
    path = f.readlines()
    for item in path:
        item = re.sub("\\n", "", item)
        paths[i] = item
        i = i + 1

totalpaths = len(paths.keys())

while currentpath <= totalpaths:
    trail = paths[currentpath].split(',')
    for direction in trail:
        if direction.startswith('R'):
            for value in range(0,int(direction[1:])):
                change = int(location['x']) + 1
                location['x'] = change
                upload = str(location['x']) + ':' + str(location['y'])
                if upload not in positions:
                    positions.append(upload)
        if direction.startswith('L'):
            for value in range(0,int(direction[1:])):
                change = int(location['x']) - 1
                location['x'] = change
                upload = str(location['x']) + ':' + str(location['y'])
                if upload not in positions:
                    positions.append(upload)
        if direction.startswith('U'):
            for value in range(0,int(direction[1:])):
                change = int(location['y']) + 1
                location['y'] = change
                upload = str(location['x']) + ':' + str(location['y'])
                if upload not in positions:
                    positions.append(upload)
        if direction.startswith('D'):
            for value in range(0,int(direction[1:])):
                change = int(location['y']) - 1
                location['y'] = change
                upload = str(location['x']) + ':' + str(location['y'])
                if upload not in positions:
                    positions.append(upload)
    location = {'x':0, 'y':0}
    paths[currentpath + totalpaths] = positions
    positions = []
    currentpath = currentpath + 1

intersections = []
lowest_intersect = 0

for position in paths[3]:
    if position in paths[4]:
        intersections.append(position)

for points in intersections:
    points = points.split(':')
    total = abs(int(points[0])) + abs(int(points[1]))
    if total <= lowest_intersect or lowest_intersect == 0:
        lowest_intersect = total

print(lowest_intersect)


