#Part 1
import re

with open('input.txt', 'r') as inp: #Check if you're in the right repository on terminal
     values = inp.read().split('\n')

ans1 = ''

dct = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],
    8 : [],
    9 : []
}


for value in values:
    if '[' in value:
        index = 1
        for i in range(1,10):
            if value[index] != ' ':
                dct[i].append(value[index])
            index += 4
    elif 'move' in value:
        times, sender, receiver = map(int, re.findall(r'\d+', value))
        for _ in range(0, times):
            dct[receiver].insert(0, dct[sender][0])
            dct[sender].pop(0)

for i in range(1,10):
    ans1 += ''.join(dct[i][0])

print(ans1)

#Part 2

ans2 = ''

dct = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],
    8 : [],
    9 : []
}

for value in values:
    if '[' in value:
        index = 1
        for i in range(1,10):
            if value[index] != ' ':
                dct[i].append(value[index])
            index += 4
    elif 'move' in value:
        moves = []
        times, sender, receiver = map(int, re.findall(r'\d+', value))
        for _ in range(0, times):
            moves += dct[sender][0]
            dct[sender].pop(0)
        
        dct[receiver][0:0] =  moves

for i in range(1,10):
    ans2 += ''.join(dct[i][0])

print(ans2)