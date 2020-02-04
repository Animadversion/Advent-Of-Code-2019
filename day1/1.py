#!/usr/bin/python3

import math

with open('/home/kiriha/advent/1/input') as f:
    data = f.read().splitlines()

# data = [12, 14,1969, 100756]
output = []
total = 0
for item in data:
    item = int(item)
    item = item / 3
    item = math.trunc(item)
    item = int(item)
    item = item - 2
    output.append(item)

for value in output:
    total = int(total) + int(value)

print(total)