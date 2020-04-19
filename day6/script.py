#!/usr/bin/env python3

import time, json

orbits = {}
edges = []
primary = 'COM'
orbitvalues = {}
reverseorbit = {}

with open('day6/input') as f:
    inputdata = f.readlines()
    f.close()

for line in inputdata:
    line = line.strip('\n')
    line = line.split(')')
    orbitee = line[0]
    orbiter = line[1]
    try:
        orbitlist = orbits[orbitee]
        orbitlist.append(orbiter)
        orbits[orbitee] = orbitlist
    except KeyError:
        orbitlist = []
        orbitlist.append(orbitee)
        orbitlist.append({"value" + orbitee : 0, 'crossed' + orbitee : 1})
        orbits[orbitee] = orbitlist
    reverseorbit[orbiter] = orbitee

for item in orbits:
    for thing in orbits[item]:
        if type(thing) != dict:
            if thing not in orbits.keys():
                edges.append(thing)

def evalfunc(item):
    path = []
    path.append(item)
    while item != primary:
        path.append(reverseorbit[item])
        item = reverseorbit[item]
    j = len(path) - 1
    
    for thing in path:
        try:
            if orbits[thing][1]['value' + thing] == 0:
                orbits[thing][1]['value' + thing] = orbits[thing][1]['value' + thing] + j
            else:
                orbits[thing][1]['crossed' + thing] = orbits[thing][1]['crossed' + thing] + 1
            j = j - 1
        except KeyError:
            continue
        


    
for item in edges:
        curritem = reverseorbit[item]
        evalfunc(item)
print(json.dumps(orbits, indent = 2))

total = 0
for item in orbits:
    total = total + (orbits[item][1]['value' + item] * orbits[item][1]['crossed' + item])
print(total)
