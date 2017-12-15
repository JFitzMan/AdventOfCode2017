direction = {}

def advancePico(firewall):
    for key, val in firewall.items():
        if val != []:
            for i in range(0, len(val)):
                if firewall[key][i] is True:
                    firewall[key][i] = False
                    if i+1 == len(val): direction[key] = -1
                    if i-1 == -1: direction[key] = 1
                    firewall[key][i+(direction[key])] = True
                    break
    return firewall



def day13():
    max = 0
    firewall = {}
    with open('day13.txt', 'r') as f:
        for line in f:
            l = list(map(int,line.replace(' ', '').strip().split(':')))
            firewall[l[0]] = l[1]
            if int(l[0]) > max: max = int(l[0])
    print(firewall)
    print(str(max))

    # Get firewall in initial state
    for key in range(0, max+1):
        if key in firewall:
            depth = firewall[key]
            firewall[key] = []
            for i in range(0, depth):
                if i == 0: firewall[key].append(True)
                else: firewall[key].append(False)
        else:
            firewall[key] = []

    for key, value in firewall.items():
        direction[key] = 1

    print(firewall)
    print(direction)
    print('\n\n')

    severity = 0
    for i in range(0, max+1):
        print('Round '+str(i))
        print(firewall)
        if firewall[i] != []:
            print(firewall[i][0])
            if (firewall[i][0]) == True:
                severity = severity + (len(firewall[i])*i)
        firewall = advancePico(firewall)
        print(firewall)
        print('\n\n')

    print(severity)

def day13_pt2():
    max = 0
    firewall = {}
    with open('day13.txt', 'r') as f:
        for line in f:
            l = list(map(int,line.replace(' ', '').strip().split(':')))
            firewall[l[0]] = l[1]
            if int(l[0]) > max: max = int(l[0])
    print(firewall)
    print(str(max))

    # Get firewall in initial state
    for key in range(0, max+1):
        if key in firewall:
            depth = firewall[key]
            firewall[key] = []
            for i in range(0, depth):
                if i == 0: firewall[key].append(True)
                else: firewall[key].append(False)
        else:
            firewall[key] = []

    for key, value in firewall.items():
        direction[key] = 1

    print(firewall)
    print(direction)
    print('\n\n')
    delay = 3850258
    severity = 0
    while True:
        print("Delay: "+str(delay))
        for key, value in firewall.items():
            direction[key] = 1
        for x in range(0, delay):
            firewall = advancePico(firewall)
        for i in range(0, max+1):
            if firewall[i] != [] and (firewall[i][0]) == True:
                break
            firewall = advancePico(firewall)
        else:
            print(delay)
            break

        #print(severity)
        delay +=1

    print('\n\n')
    print(delay)



def day13Reddit():
    lines = [x.rstrip().split(': ') for x in open('day13.txt', 'r')]
    print(lines)
    delay = 1
    while delay:
        s = 0
        for line in lines:
            line = [int(x) for x in line]
            sev = (delay + line[0]) % ((line[1] - 1) * 2)
            if not sev:
                s += line[0] * line[1]
                break
        else:
            print(delay)
            break
        delay += 1

day13_pt2()