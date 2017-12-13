import operator as op
def day11():
    with open('day11.txt', 'r') as f:
        line = f.readline().split(',')

    steps = { 'n':  (0, 1, -1),
             'ne':  (1, 0, -1),
             'se':  (1, -1, 0),
              's':  (0, -1, 1),
             'sw':  (-1, 0, 1),
             'nw':  (-1, 1, 0),}
    cur = (0,0,0)
    distance = 0
    for x in line:
        cur = tuple(map(op.add, cur, steps[x]))
        if max(map(op.abs, cur)) > distance:
            distance = max(map(op.abs, cur))
    print(max(map(op.abs, cur)))
    print("furthest: "+str(distance))

day11()