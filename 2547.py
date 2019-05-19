import math

while True:
    try:
        a, b, c = raw_input().split(' ')
        a = int(a)
        b = int(b)
        c = int(c)
        d = 0

        for i in range(a):
            x = input()
            if x >= b and x <= c:
                d += 1

        print d
    except EOFError:
        break
