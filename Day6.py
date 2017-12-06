from collections import defaultdict
def day6():
    states = defaultdict(bool)
    with open('day6.txt', 'r') as f:
        input = f.readline().strip().split()
        input = list(map(int, input))
        inLen = len(input)
        inString = ','.join(str(e) for e in input)
        answer = 0
        while states[inString] is False:
            # mark this state as seen
            states[inString] = True
            #get the current max and its index
            max = input[0]
            maxIndex = 0
            for x in range(len(input)):
                if input[x]>max:
                    max = input[x]
                    maxIndex = x
            input[maxIndex] = 0
            for i in range(1,max+1):
                maxIndex += 1
                input[maxIndex%inLen] += 1
            inString = ','.join(str(e) for e in input)
            answer+=1
        return answer

def day6_pt2():
    states = defaultdict(bool)
    with open('day6.txt', 'r') as f:
        input = f.readline().strip().split()
        input = list(map(int, input))
        inLen = len(input)
        inString = ','.join(str(e) for e in input)
        answer = 0
        cycle = []
        while states[inString] is False:
            # mark this state as seen
            states[inString] = True
            cycle.append(inString)
            #get the current max and its index
            max = input[0]
            maxIndex = 0
            for x in range(len(input)):
                if input[x]>max:
                    max = input[x]
                    maxIndex = x
            input[maxIndex] = 0
            for i in range(1,max+1):
                maxIndex += 1
                input[maxIndex%inLen] += 1
            inString = ','.join(str(e) for e in input)
            answer+=1
        return answer-cycle.index(inString)




print(day6())
print(day6_pt2())

