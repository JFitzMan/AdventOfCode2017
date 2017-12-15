def padBin(bin):
    for i in range(0, 16):
        if i == len(bin):
            bin = ''.join(reversed(bin))
            bin+=('0')
            bin = ''.join(reversed(bin))
    return bin


def day15():
    A = 0
    B = 1
    value = []
    factor = []
    value.append([x.rstrip().split(' ') for x in open('day15.txt', 'r')][0][-1])
    value.append(([x.rstrip().split(' ') for x in open('day15.txt', 'r')][1])[-1])
    value = list(map(int, value))
    factor.append(16807)
    factor.append(48271)
    print("A: " + str(value[A]) + "\tfactor " + str(factor[A]))
    print("B: " + str(value[B]) + "\tfactor " + str(factor[B]))

    matchA = []
    matchB = []
    match = 0
    count = 0
    moreA = True
    moreB = True
    while moreA or moreB:
        if moreA and len(matchA) <= 5000000:
            value[A] = (value[A] * factor[A]) % 2147483647
            if value[A]%4 == 0:
                matchA.append(padBin("{0:b}".format(value[A])))
        else:
            moreA = False

        if moreB and len(matchB) <= 5000000:
            value[B] = (value[B] * factor[B]) % 2147483647
            if value[B] % 8 == 0:
                matchB.append(padBin("{0:b}".format(value[B])))
        else:
            moreB = False
    for x in range(0, len(matchA)):
        if matchA[x][-16:] == matchB[x][-16:]:
            match+=1
    print(match)

day15()
