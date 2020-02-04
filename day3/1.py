#!/usr/bin/python3

import time, json

location = {'x':0, 'y':0}
path = []
paths = {}
varulable = 0

with open('/home/kiriha/advent/day3/input') as f:
    input = f.read()
    input = input.split('\n')
    for thing in input:
        thing = thing.split(',')


        for item in thing:
            if item.startswith('R'):
                for value in range(0,int(item[1:])):
                    change = int(location['x']) + 1
                    location['x'] = change
                    upload = str(location['x']) + ':' + str(location['y'])
                    if upload not in path:
                        path.append(upload)
            if item.startswith('L'):
                for value in range(0,int(item[1:])):
                    change = int(location['x']) - 1
                    location['x'] = change
                    upload = str(location['x']) + ':' + str(location['y'])
                    if upload not in path:
                        path.append(upload)
            if item.startswith('U'):
                for value in range(0,int(item[1:])):
                    change = int(location['y']) + 1
                    location['y'] = change
                    upload = str(location['x']) + ':' + str(location['y'])
                    if upload not in path:
                        path.append(upload)
            if item.startswith('D'):
                for value in range(0,int(item[1:])):
                    change = int(location['y']) - 1
                    location['y'] = change
                    upload = str(location['x']) + ':' + str(location['y'])
                    if upload not in path:
                        path.append(upload)
        print('done')
        paths[varulable + 1] = path
        varulable = varulable + 1
        print(paths[varulable])
        # with open('output', 'a') as f:
        #     f.write(str(path1))
        #     f.write('\n\n\n\n\n\n\n\n\n')
        path = []
        location = {'x':0, 'y':0}

