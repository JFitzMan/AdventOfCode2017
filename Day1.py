def day1():
    i = str(input('input: '))
    length = len(i)
    c = sum1 = sum2 = 0
    while c < length:
        if i[c] == i[(c+1)%length]:
            sum1 += int(i[c])
        if i[c] == i[int((c+(length/2))%length)]:
            sum2 += int(i[c])
        c += 1
    print("Sum Part 1: "+str(sum1)+"\nSum Part 2: "+str(sum2))


def day1_zolrathReddit(nums, part_b=False):
    step = len(nums) // 2 if part_b else 1
    return sum(int(a) for a, b in zip(nums, nums[step:] + nums[:step]) if a == b)

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
