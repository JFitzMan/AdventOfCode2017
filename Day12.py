import re
from collections import defaultdict

dict = defaultdict(bool)
pipes = {}

def scanChildren(start, level):
    if dict[start] == True:
        return level
    dict[start] = True
    for child in pipes[start]:
        scanChildren(child, level+1)

def day12():
    regex = re.compile(r'(\d+) <-> ([\d ,]+)')
    with open('day12.txt', 'r') as f:
        for line in f:
            match = regex.match(line)
            parent = int(match.group(1))
            children = list(map(int, match.group(2).split(',')))
            pipes[parent] = children
    #print(pipes)
    scanChildren(0)
    print(dict)
    total = 0
    for x, y in dict.items():
        total+=1
    print(total)

def day12_pt2():
    regex = re.compile(r'(\d+) <-> ([\d ,]+)')
    with open('day12.txt', 'r') as f:
        for line in f:
            match = regex.match(line)
            parent = int(match.group(1))
            children = list(map(int, match.group(2).split(',')))
            pipes[parent] = children

    count = 0
    for x, y in pipes.items():
        level = scanChildren(x, 0)
        if level != 0:
            count+=1
    print(dict)
    total = 0
    for x, y in dict.items():
        total+=1
    print(count)



day12_pt2()