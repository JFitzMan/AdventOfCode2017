import re
from collections import defaultdict

class Node:
    name = ''
    children = []
    parent = ''
    weight = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = ''

    def addChild(self, child):
        self.children.append(child)

    def getName(self):
        return self.name

    def getChildren(self):
        return self.children

    def getWeight(self):
        return self.weight

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def weightOfTower(self, nodes, space=''):
        sum = int(self.weight)
        for c in self.children:
            print("         name: " + nodes[c].getName() + "\tweight: " + str(nodes[c].getWeight()))
            sum += int(nodes[c].weightOfTower(nodes, space+' '))
        return sum

    def weightOfChildTowers(self, nodes):
        vals = []
        for c in self.children:
            vals.append(int(nodes[c].weightOfTower(nodes)))
        return vals

    def weightOfChildTowers2(self, nodes):
        vals = []
        for c in self.children:
            print("name: "+nodes[c].getName()+"\tweight: "+str(nodes[c].getWeight()))
            vals.append(int(nodes[c].weightOfTower(nodes)))
        return vals


def checkEqual(iterator):
   return len(set(iterator)) <= 1

def day7():
    regex = re.compile(r'^(\w+) \((\d+)\)(?: -> ([\w, ]+))?')
    parent = defaultdict(bool)
    with open('day7.txt', 'r') as f:
        for line in f:
            m = regex.match(line)
            parent[m.group(1).strip()]
            if m.group(3) is not None:
                for proc in m.group(3).split(','):
                    parent[proc.strip()] = True
        for name, parentStatus in parent.items():
            if parentStatus is False:
                print(name)

def day7_pt2():
    regex = re.compile(r'^(\w+) \((\d+)\)(?: -> ([\w, ]+))?')
    nodes = {}
    node = None
    with open('day7.txt', 'r') as f:
        # Populate dictionary with node names, weights, and children
        for line in f:
            m = regex.match(line)
            # Group 1 is name, group 2 is weight
            node = Node(m.group(1), m.group(2))
            nodes[m.group(1)] = node
            if m.group(3) is not None:
                for proc in m.group(3).split(','):
                    node.addChild(proc.strip())

        # Populate parents
        for name, node in nodes.items():
            children = node.getChildren()
            if len(children) > 0:
                for c in children:
                    if c in nodes:
                        nodes[c].setParent(name)

        for name, node in nodes.items():
            if checkEqual(node.weightOfChildTowers(nodes)) is False:
                print()
                print()
                print(node.weightOfChildTowers2(nodes))
                print(name)

#day7()
day7_pt2()
# Three answers are output. This is because each tower that is built on the unbalanced tower is also unbalanced. The one that would need to change is the smallest weight
