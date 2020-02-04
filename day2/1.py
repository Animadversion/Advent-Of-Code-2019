#!/usr/bin/python3

import time

global iAmAt
opCode = 0
iAmAt = 0
newData = []

with open('input') as f:
    data = f.read()
    data = data.replace('\n', '')
    data = data.split(',')
# data = [1,9,10,3,2,3,11,0,99,30,40,50]
# data = [2,4,4,5,99,0]
# data = [1,1,1,4,99,5,6,0,99]

def voomList(whereTo):
    global iAmAt, data
    data = []
    iAmAt = 0
    # time.sleep(5)
    for item in current:
        if int(iAmAt) == int(whereTo):
            data.append(output)
        elif int(iAmAt) != int(whereTo):
            data.append(item)
        iAmAt = iAmAt + 1

while True:
    try:
        current = data
        code = int(data[opCode])
        if code == 1:
            valueOne = int(data[opCode + 1])
            valueTwo =  int(data[opCode + 2])
            output = int(data[valueOne]) + int(data[valueTwo])
            whereTo = int(data[opCode + 3])
            voomList(whereTo = whereTo)
            current = data
        elif code == 2:
            valueOne = int(data[opCode + 1])
            valueTwo =  int(data[opCode + 2])
            output = int(data[valueOne]) * int(data[valueTwo])
            whereTo = int(data[opCode + 3])
            voomList(whereTo = whereTo)
            current = data
        elif code == 99:
            print('breaking')
            break
        else:
            print('you fucked up')
        opCode = opCode + 4
    except IndexError:
        print('error')
        break
print(data[0])