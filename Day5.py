def day5(pt2=False):
    jumps = []
    with open('day5.txt', 'r') as f:
        for line in f:
            jumps.append(line.strip())
        jumps = list(map(int, jumps))
        x = 0
        count = 0
        while x < len(jumps) and x >= 0:
            next = jumps[x]
            if next >= 3 and pt2: jumps[x]-= 1
            else: jumps[x]+= 1
            x+=next
            count+=1
        return count


print(day5())
print(day5(pt2=True))