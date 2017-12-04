def day4():
    validCount = 0
    with open('day4.txt', 'r') as f:
        for line in f:
            words = line.split()
            if len(words) == len(set(words)): # set() removes duplicates
                validCount+=1
    return validCount

def day4_pt2():
    def noAnagram(l):
        for i in range(len(l)):
            l[i] = ''.join(sorted(l[i])) # Sort each individual word, then anagrams become duplicates
        if len(l) == len(set(l)): return True
        else: return False

    validCount = 0
    with open('day4.txt', 'r') as f:
        for line in f:
            words = line.split()
            if len(words) == len(set(words)) and noAnagram(words): # set() removes duplicates
                validCount+=1
    return validCount

print(day4())
print(day4_pt2())
