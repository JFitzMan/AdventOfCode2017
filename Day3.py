# 37  36  35  34  33  32  31
# 38  17  16  15  14  13  30
# 39  18   5   4   3  12  29
# 40  19   6   1   2  11  28
# 41  20   7   8   9  10  27
# 42  21  22  23  24  25  26
# 43  44  45  46  47  48  49

#1R 1U 2L 2D 3R 3U 4L 4D 5R 5U 6L 6D

#R = positiveX
#L = negativeX
#U = positiveY
#D = negativeY
#RULD repeating
#1 (0,0)
#2 (1,0) 1R
#3 (1,1) 1U
#4 (0,1) 2L
#5 (-1,1)

def day3(top = 289326):
    current = 1
    count = 1
    x = 0
    y = 0
    spiral = {}
    spiral[current] = (x,y)
    while current <= top:
        #R
        for i in range(count):
            current += 1
            x += 1
            spiral[current] = (x,y)
        #U
        for i in range(count):
            current += 1
            y += 1
            spiral[current] = (x, y)
        count += 1
        # L
        for i in range(count):
            current+= 1
            x -= 1
            spiral[current] = (x, y)
        #D
        for i in range(count):
            current+= 1
            y -= 1
            spiral[current] = (x, y)

        count += 1
    print(abs(spiral[289326][0])+abs(spiral[289326][1]))

day3()


