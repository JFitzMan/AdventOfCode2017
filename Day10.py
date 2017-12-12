def rotate(l, n):
    return l[n:]+l[:n]

def convertToASCII(string):
    ascii = []
    for c in string:
        ascii.append(ord(c))
    return ascii+[17, 31, 73, 47, 23]

def denseHash(l):
    result = l[0]
    for x in l[1:]:
        result = result ^ x
    return result

def toHex(l):
    out = ''
    for c in l:
        out+=format(int(c), '02x')
    return out


def day10():
    totalNums = 256
    #totalNums = 5
    with open('day10.txt', 'r') as f:
        line = f.readline()
    input = convertToASCII(line)
    nums = list(range(totalNums))
    curPos = skipSize = 0
    round = 0
    while round < 64:
        for length in input:
            #rotate list to make curPos always the first element
            nums = rotate(nums, curPos)
            #reverse that section of the list
            nums[:length] = reversed(nums[:length])
            #rotate back the rest of the way
            nums = rotate(nums, (len(nums)-curPos))
            #updates made according to rules
            curPos = (curPos + length + skipSize)%len(nums)
            skipSize += 1
        round += 1

    count = 1
    dense = []
    while count <= 256:
        if count%16 == 0:
            dense.append(denseHash(nums[count-16:count]))
        count += 1
    print(toHex(dense))

day10()
