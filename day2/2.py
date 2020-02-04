#!/usr/bin/python3

import time, sys

# bash loop to find answer 
# for item in $(seq 0 100); do for item2 in $(seq 0 100); do ./2.py $item $item2;done;done > output
# cat output  | grep 19690720

global iAmAt, noun, verb, opCode
opCode = 0
iAmAt = 0

with open('/home/kiriha/advent/day2/input') as f:
    input = f.read()
    input = input.replace('\n', '')
    input = input.split(',')

try:
    noun = sys.argv[1]
    verb = sys.argv[2]
except:
    print('gno')
    exit()
data = []
data.append(1)
data.append(int(noun))
data.append(int(verb))
for item in input[3:]:
    data.append(item)


def voomList(whereTo):
    global iAmAt, data
    data = []
    iAmAt = 0
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
            break
        else:
            print('you fucked up')
            exit()
        opCode = opCode + 4
    except IndexError:
        print('error')
        break
print(str(data[0]) + ' ' + str(noun) + ' ' + str(verb) + ' ' + str((1000 * int(noun) + int(verb))))
