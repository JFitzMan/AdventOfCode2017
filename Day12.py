import re
from collections import defaultdict

dict = defaultdict(bool)
pipes = {}

def scanChildren(start, level=0):
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

    scanChildren(0)
    total = 0
    for x, y in dict.items():
        total+=1
    print('Total in group with 0: '+str(total))

    count = 0
    for x, y in pipes.items():
        level = scanChildren(x)
        if level != 0:
            count += 1
    print('Total groups: ' + str(count))


day12()