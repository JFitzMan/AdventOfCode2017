def day9():
    with open('day9.txt', 'r') as f:
        line = f.readline()
    curScore = 0
    totalScore = 0
    escape = False
    garbage = False
    totalGarbage = 0
    for c in line:
        if escape:
            escape = False
            continue
        if c == '{' and not garbage:
            curScore += 1
            totalScore += curScore
        elif c == '}' and not garbage:
            curScore -= 1
        elif c == '!':
            escape = True
        elif c == '<' and not garbage:
            garbage = True
        elif c == '>' and garbage:
            garbage = False
        elif garbage:
            totalGarbage += 1
    print("Score: "+str(totalScore)+"\tGarbage removed: "+str(totalGarbage))
day9()