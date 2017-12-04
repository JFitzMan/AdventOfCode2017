def day2():
    checkSum1 = 0
    checkSum2 = 0
    with open('day2.txt', 'r') as f:
        for line in f:
            l = line.split()
            l = list(map(int, l))
            checkSum1 += (max(l) - min(l))

            for i in range(len(l)):
                for j in range(len(l)):
                    if i == j: continue
                    if l[i]%l[j] == 0:
                        checkSum2 += l[i]/l[j]

    print("Part 1: "+str(checkSum1)+'  Part 2: '+str(checkSum2))

day2()
