#!/usr/bin/python3

import math

output = []
total = 0

with open('input') as f:
    data = f.read().splitlines()

def mainfunc(thing, code):
    item = thing / 3
    item = math.trunc(item)
    item = int(item)
    item = item - 2
    if code == 2 and item > 0:
        mainfunc(thing = item, code = code)
        output.append(item)
    elif code == 1:
        output.append(item)

for x in range(1,3):
    global item
    for item in data:
        item = int(item)
        mainfunc(thing = item, code = x)
    for value in output:
        total = int(total) + int(value)
    print("puzzle" + str(x) + ": " + str(total))
    total = 0
    output = []

