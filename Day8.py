from collections import defaultdict
import re
import operator

def day8():
    ops = {">": operator.gt,
           ">=": operator.ge,
           "<": operator.lt,
           "<=": operator.le,
           "==": operator.eq,
           "!=": operator.ne,
           "inc": operator.add,
           "dec": operator.neg,}

    regex = re.compile(r'^(\w+) (inc|dec) (-?\d+) if (\w+) ([><=!]+) (-?\d+)$')
    reg = defaultdict(int)
    globalMax = 0
    with open('day8.txt', 'r') as f:
        for line in f:
            match = regex.match(line)
            toEdit = match.group(1)
            op = match.group(2)
            amount = int(match.group(3))
            condReg = match.group(4)
            cond = match.group(5)
            condNum = int(match.group(6))

            if ops[cond](reg[condReg], condNum):
                #print(line)
                if op == 'dec':
                    amount = operator.neg(amount)
                reg[toEdit] += amount
                if reg[toEdit] > globalMax:
                    globalMax = reg[toEdit]

    max = reg[0]
    for key, val in reg.items():
        if val > max:
            max = val
    print("Current max: "+str(max)+"\tGlobal max: "+str(globalMax))


day8()
