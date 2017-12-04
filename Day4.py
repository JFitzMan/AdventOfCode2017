def day4():
    validCount = 0
    with open('day4.txt', 'r') as f:
        for line in f:
            words = line.split()
            if len(words) == len(set(words)): # set() removes duplicates
                validCount+=1
    return validCount

def day4_pt2():
    validCount = 0
    with open('day4.txt', 'r') as f:
        for line in f:
            words = line.split()
            for i in range(len(words)):
                words[i] = ''.join(sorted(words[i]))  # Sort each individual word, then anagrams become duplicates
            if len(words) == len(set(words)):
                validCount+=1
    return validCount

print(day4())
print(day4_pt2())
