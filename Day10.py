def rotate(l, n):
    return l[n:]+l[:n]

def day10():
    totalNums = 256
    #totalNums = 5
    with open('day10.txt', 'r') as f:
        line = f.readline()
    input = list(map(int, line.split(',')))
    nums = list(range(totalNums))
    curPos = skipSize = 0
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

    print(nums[0]*nums[1])

day10()