import re
from collections import defaultdict
def day7():
    regex = re.compile(r'^(\w+) \((\d+)\)(?: -> ([\w, ]+))?')
    parent = defaultdict(bool)
    with open('day7.txt', 'r') as f:
        for line in f:
            m = regex.match(line)
            print(m.group(1))
            parent[m.group(1).strip()]
            print(m.group(2))
            if m.group(3) is not None:
                print(m.group(3).split(','))
                for proc in m.group(3).split(','):
                    parent[proc.strip()] = True
        for name, parentStatus in parent.items():
            if parentStatus is False:
                print(name)

day7()
