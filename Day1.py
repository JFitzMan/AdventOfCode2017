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
